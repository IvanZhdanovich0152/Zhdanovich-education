public class HighSpeedRollGate extends GateController {
    private int PressurePneumaticSafetyEdge;
    private int wearPVCMembrane;

    public static OperationResult<HighSpeedRollGate> create(
            int numberCheckpoint,
            boolean isOperating,
            TypeLockState lockState,
            int PressurePneumaticSafetyEdge,
            int wearPVCMembrane
    ) {
        if (numberCheckpoint <= 0) {
            return OperationResult.fail("Номер КПП должен быть положительным.");
        }
        if (lockState == null) {
            return OperationResult.fail("Состояние шлюза не может быть null.");
        }
        if (PressurePneumaticSafetyEdge <= 0) {
            return OperationResult.fail("Давление пневматической кромки должно быть положительным.");
        }
        if (wearPVCMembrane < 0 || wearPVCMembrane > 100) {
            return OperationResult.fail("Износ ПВХ-мембраны должен быть от 0 до 100 процентов.");
        }
        return OperationResult.ok(
                new HighSpeedRollGate(
                        numberCheckpoint,
                        isOperating,
                        lockState,
                        PressurePneumaticSafetyEdge,
                        wearPVCMembrane
                ),
                "Скоростные рулонные ворота успешно созданы."
        );
    }

    private HighSpeedRollGate(
             int numberCheckpoint,
             boolean isOperating,
             TypeLockState lockState,
             int PressurePneumaticSafetyEdge,
             int wearPVCMembrane
    ) {
        super(numberCheckpoint, isOperating, lockState);

        this.PressurePneumaticSafetyEdge = PressurePneumaticSafetyEdge;
        this.wearPVCMembrane = wearPVCMembrane;
    }

    @Override
    public OperationResult<Void> startOpening() {
        OperationResult<Void> validationResult = validateOpening();
        if (validationResult != null) {
            return validationResult;
        }
        if (wearPVCMembrane >= 100) {
            return OperationResult.fail("Рулонные ворота не открыты [ПВХ-мембрана полностью изношена].");
        }
        if (lockState == TypeLockState.UNLOCKED) {
            return OperationResult.fail("Скоростные рулонные ворота уже открыты.");
        }
        lockState = TypeLockState.UNLOCKED;
        return OperationResult.ok("Скоростные рулонные ворота открыты пневматической кромкой.");
    }

    @Override
    public OperationResult<Void> startClosing() {
        OperationResult<Void> validationResult = validateClosing();
        if (validationResult != null) {
            return validationResult;
        }
        if (wearPVCMembrane >= 100) {
            return OperationResult.fail("Рулонные ворота не закрыты [ПВХ-мембрана полностью изношена].");
        }
        if (lockState == TypeLockState.ARMED_BLOCK) {
            return OperationResult.fail("Скоростные рулонные ворота уже закрыты.");
        }
        lockState = TypeLockState.ARMED_BLOCK;
        return OperationResult.ok("Скоростные рулонные ворота закрыты при давлении "
                + PressurePneumaticSafetyEdge + ".");
    }

    public OperationResult<Void> heatRollMechanism() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        if (wearPVCMembrane >= 100) {
            return OperationResult.fail("Подогрев не включён [ПВХ-мембрана полностью изношена].");
        }
        return OperationResult.ok("Включен подогрев вала для предотвращения обледенения зимой.");
    }

    public OperationResult<Void> replacePVCMembrane(int newWear) {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        if (newWear < 0 || newWear > 100) {
            return OperationResult.fail("Износ ПВХ-полотна должен быть от 0 до 100 процентов.");
        }
        wearPVCMembrane = newWear;
        return OperationResult.ok("Состояние ПВХ-полотна обновлено.");
    }

    @Override
    public OperationResult<Void> modifyGate(int amount) {
        return replacePVCMembrane(amount);
    }



    @Override
    public String toString() {
        return super.toString() + "\n"
                + "Давление в пневматической кромке - " + PressurePneumaticSafetyEdge + "\n"
                + "Износ ПВХ-полотна - " + wearPVCMembrane + "%";
    }
}
