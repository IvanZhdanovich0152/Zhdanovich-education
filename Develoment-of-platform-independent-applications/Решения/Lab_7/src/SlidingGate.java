public class SlidingGate extends GateController {
    private int openingPosition;
    private int timingBeltTension;

    public static OperationResult<SlidingGate> create(
            int numberCheckpoint,
            boolean isOperating,
            TypeLockState lockState,
            int openingPosition,
            int timingBeltTension
    ) {
        if (numberCheckpoint <= 0) {
            return OperationResult.fail("Номер КПП должен быть положительным.");
        }
        if (lockState == null) {
            return OperationResult.fail("Состояние шлюза не может быть null.");
        }
        if (openingPosition < 0 || openingPosition > 100) {
            return OperationResult.fail("Положение створки должно быть от 0 до 100 процентов.");
        }
        if (timingBeltTension < 0) {
            return OperationResult.fail("Натяжение ремня не может быть отрицательным.");
        }
        return OperationResult.ok(
                new SlidingGate(
                        numberCheckpoint,
                        isOperating,
                        lockState,
                        openingPosition,
                        timingBeltTension
                ),
                "Откатные ворота успешно созданы."
        );
    }

    private SlidingGate(
             int numberCheckpoint,
             boolean isOperating,
             TypeLockState lockState,
             int openingPosition,
             int timingBeltTension
    ) {
        super(numberCheckpoint, isOperating, lockState);

        this.openingPosition = openingPosition;
        this.timingBeltTension = timingBeltTension;
    }

    @Override
    public OperationResult<Void> startOpening() {
        OperationResult<Void> validationResult = validateOpening();
        if (validationResult != null) {
            return validationResult;
        }
        if (lockState == TypeLockState.UNLOCKED) {
            return OperationResult.fail("Откатные ворота уже открыты.");
        }
        openingPosition = 100;
        lockState = TypeLockState.UNLOCKED;
        return OperationResult.ok("Откатные ворота открыты на 100 процентов.");
    }

    @Override
    public OperationResult<Void> startClosing() {
        OperationResult<Void> validationResult = validateClosing();
        if (validationResult != null) {
            return validationResult;
        }
        if (lockState == TypeLockState.ARMED_BLOCK) {
            return OperationResult.fail("Откатные ворота уже закрыты.");
        }
        openingPosition = 0;
        lockState = TypeLockState.ARMED_BLOCK;
        return OperationResult.ok("Откатные ворота закрыты, натяжение ремня проверено.");
    }

    public OperationResult<Void> checkLimitSwitches() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        OperationResult<Void> resultTestPhotocells = testPhotocells();
        if (!resultTestPhotocells.isSuccess()) {
            return resultTestPhotocells;
        }
        return OperationResult.ok("Калибровка конечных выключателей хода створки запущена.");
    }

    public OperationResult<Void> adjustTimingBelt(int amount) {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        if (timingBeltTension + amount < 0) {
            return OperationResult.fail("Натяжение ремня не может быть отрицательным.");
        }
        timingBeltTension += amount;
        return OperationResult.ok("Натяжение зубчатого ремня изменено на " + amount + ".");
    }

    @Override
    public OperationResult<Void> modifyGate(int amount) {
        return adjustTimingBelt(amount);
    }


    @Override
    public String toString() {
        return super.toString() + "\n"
                + "Положение створки - " + openingPosition + "%\n"
                + "Натяжение зубчатого ремня - " + timingBeltTension;
    }
}
