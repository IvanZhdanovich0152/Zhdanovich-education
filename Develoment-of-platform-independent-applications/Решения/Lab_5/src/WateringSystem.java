public class WateringSystem implements SimpleWateringSystem {
    public enum WaterState {NOT_WATERING, LOW_WATERING, MID_WATERING, HARD_WATERING}

    private int waterTank;
    private final int MaxWaterTank;
    private int moistureLevel;
    private WaterState isActive;

    private WateringSystem(int waterTank, int MaxWaterTank, int moistureLevel, WaterState waterState) {
        this.waterTank = waterTank;
        this.MaxWaterTank = MaxWaterTank;
        this.moistureLevel = moistureLevel;
        this.isActive = waterState;
    }

    public static OperationResult<WateringSystem> create(int waterTank, int MaxWaterTank, int moistureLevel, WaterState waterState) {
        if (waterState == null) {
            return OperationResult.fail("Состояние воды (waterState) не может быть null.");
        }
        if (MaxWaterTank <= 0) {
            return OperationResult.fail("Максимальный объем бака (MaxWaterTank) должен быть больше 0.");
        }
        if (waterTank < 0) {
            return OperationResult.fail("Текущий объем воды (waterTank) не может быть отрицательным.");
        }
        if (waterTank > MaxWaterTank) {
            return OperationResult.fail(
                    "Текущий объем воды ("+waterTank+") не может превышать максимальный ("+MaxWaterTank+")."  );
        }
        if (moistureLevel < 0 || moistureLevel > 100) {
            return OperationResult.fail( "Уровень влажности (moistureLevel) должен быть в диапазоне от 0% до 100%.");
        }
        var wateringSystem = new WateringSystem(waterTank, MaxWaterTank, moistureLevel, waterState);
        return OperationResult.ok(wateringSystem, "Система полива почвы успешно создан.");
    }

    @Override
    public OperationResult<Void> water(int durationMinutes) {
        if (isActive != WaterState.NOT_WATERING) {
            return OperationResult.fail("Полив уже идёт.");
        }
        if (moistureLevel > 80) {
            return OperationResult.fail("Почва достаточно влажная (" + moistureLevel + "%), полив не требуется.");
        }
        if (durationMinutes * 5 > waterTank) {
            return OperationResult.fail(
                    "В баке не хватает воды на ["+
                    durationMinutes +"] минут полива. Доступно: ["+ waterTank +"] л.");
        }
        this.isActive = WaterState.MID_WATERING;
        this.waterTank -= durationMinutes * 5;
        this.moistureLevel = Math.min(100, moistureLevel + durationMinutes * 5);
        this.isActive = WaterState.NOT_WATERING;

        return OperationResult.ok(
                "Полив завершен. Остаток воды: ["+ waterTank +"] л. Новая влажность:[" + moistureLevel+"]%.");
    }

    @Override
    public OperationResult<Void> fillTank(int liters) {
        waterTank = Math.min(MaxWaterTank, waterTank + liters);
        return OperationResult.ok("Бак пополнен. Текущий объем: ["+ waterTank +"] л.");
    }

    @Override
    public OperationResult<Void> toggleWaterState() {
        this.isActive = (this.isActive == WaterState.NOT_WATERING) ? WaterState.MID_WATERING : WaterState.NOT_WATERING;
        return OperationResult.ok("Состояние полива теперь ["+ isActive +"]");
    }

    @Override
    public void showStatus() {
        System.out.printf(
                "Система полива: Влажность почвы [%d%%], Бак с водой [%d/%d], Текущее состояние [%s]%n",
                moistureLevel, waterTank, MaxWaterTank, isActive);
    }

}
