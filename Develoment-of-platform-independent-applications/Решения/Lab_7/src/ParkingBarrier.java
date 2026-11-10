public class ParkingBarrier extends GateController {
    public enum TypeStateLED {GREEN, RED, OFF}
    private int boomElevationAngle;
    private TypeStateLED stateLED;

    public static OperationResult<ParkingBarrier> create(
            int numberCheckpoint,
            boolean isOperating,
            TypeLockState lockState,
            int boomElevationAngle,
            TypeStateLED stateLED
    ) {
        if (numberCheckpoint <= 0) {
            return OperationResult.fail("Номер КПП должен быть положительным.");
        }
        if (lockState == null) {
            return OperationResult.fail("Состояние шлюза не может быть null.");
        }
        if (boomElevationAngle < 0 || boomElevationAngle > 90) {
            return OperationResult.fail("Угол подъёма стрелы должен быть от 0 до 90 градусов.");
        }
        if (stateLED == null) {
            return OperationResult.fail("Состояние светодиода не может быть null.");
        }
        return OperationResult.ok(
                new ParkingBarrier(
                        numberCheckpoint,
                        isOperating,
                        lockState,
                        boomElevationAngle,
                        stateLED
                ),
                "Шлагбаум успешно создан."
        );
    }

    private ParkingBarrier(
             int numberCheckpoint,
             boolean isOperating,
             TypeLockState lockState,
             int boomElevationAngle,
             TypeStateLED stateLED
    ) {
        super(numberCheckpoint, isOperating, lockState);

        this.boomElevationAngle = boomElevationAngle;
        this.stateLED = stateLED;
    }

    @Override
    public OperationResult<Void> startOpening() {
        OperationResult<Void> validationResult = validateOpening();
        if (validationResult != null) {
            return validationResult;
        }
        if (lockState == TypeLockState.UNLOCKED) {
            return OperationResult.fail("Шлагбаум уже поднят.");
        }
        boomElevationAngle = 90;
        stateLED = TypeStateLED.GREEN;
        lockState = TypeLockState.UNLOCKED;
        return OperationResult.ok("Шлагбаум поднят, зелёный сигнал включён.");
    }

    @Override
    public OperationResult<Void> startClosing() {
        OperationResult<Void> validationResult = validateClosing();
        if (validationResult != null) {
            return validationResult;
        }
        if (lockState == TypeLockState.ARMED_BLOCK) {
            return OperationResult.fail("Шлагбаум уже опущен.");
        }
        boomElevationAngle = 0;
        stateLED = TypeStateLED.RED;
        lockState = TypeLockState.ARMED_BLOCK;
        return OperationResult.ok("Шлагбаум опущен, красный сигнал включён.");
    }

    public OperationResult<Void> detachBoomArm() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        boomElevationAngle = 90;
        stateLED = TypeStateLED.GREEN;
        OperationResult<Void> resultOpening = startOpening();
        if (resultOpening.isSuccess()) {
            testPhotocells();
            return OperationResult.ok("Отстрел стрелы произошёл. Проведена диагностика оптических датчиков.");
        }
        return resultOpening;
    }

    public OperationResult<Void> resetBoomSensor() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        boomElevationAngle = 0;
        stateLED = TypeStateLED.RED;
        lockState = TypeLockState.ARMED_BLOCK;
        return OperationResult.ok("Датчик стрелы сброшен, шлагбаум установлен в закрытое состояние.");
    }

    @Override
    public OperationResult<Void> modifyGate(int amount) {
        return resetBoomSensor();
    }



    @Override
    public String toString() {
        return super.toString() + "\n"
                + "Угол подъёма стрелы - " + boomElevationAngle + " градусов\n"
                + "Состояние светодиода - " + stateLED;
    }
}
