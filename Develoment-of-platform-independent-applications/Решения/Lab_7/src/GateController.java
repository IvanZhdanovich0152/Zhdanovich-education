public abstract class GateController {
    public enum TypeLockState {ARMED_BLOCK, UNLOCKED}

    protected int numberCheckpoint;
    protected boolean isOperating;
    protected TypeLockState lockState;

    protected GateController(int numberCheckpoint, boolean isOperating, TypeLockState lockState) {
        this.numberCheckpoint = numberCheckpoint;
        this.isOperating = isOperating;
        this.lockState = lockState;
    }

    protected OperationResult<Void> ensureOperating() {
        if (!isOperating) {
            isOperating = true;
        }
        return null;
    }

    public abstract OperationResult<Void> modifyGate(int amount);



    public abstract OperationResult<Void> startOpening();

    public abstract OperationResult<Void> startClosing();

    public OperationResult<Void> testPhotocells() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        return OperationResult.ok("Автодиагностика оптических датчиков проведена.");
    }

    protected OperationResult<Void> validateOpening() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        return null;
    }

    protected OperationResult<Void> validateClosing() {
        OperationResult<Void> operatingResult = ensureOperating();
        if (operatingResult != null) {
            return operatingResult;
        }
        return null;
    }

    public OperationResult<Void> setOperating(boolean operating) {
        isOperating = operating;
        return OperationResult.ok(operating
                ? "Электропривод включён."
                : "Электропривод выключен.");
    }

    @Override
    public String toString() {
        return "Номер КПП - " + numberCheckpoint + "\n"
                + "Состояние работы электропривода - " + isOperating + "\n"
                + "Состояние шлюза безопасности - " + lockState;
    }
}
