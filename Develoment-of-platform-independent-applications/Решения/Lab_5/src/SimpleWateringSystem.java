public interface SimpleWateringSystem {
    OperationResult<Void> water(int durationMinutes);
    OperationResult<Void> fillTank(int liters);
    OperationResult<Void> toggleWaterState();
    void showStatus();
}
