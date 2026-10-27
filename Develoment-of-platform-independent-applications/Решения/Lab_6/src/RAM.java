public class RAM {
    public enum TypeRAM {DDR3, DDR4, DDR5}

    private final int speed;
    private final double totalGB;
    private double usageGB = 0;
    private final TypeRAM type;

    public RAM(int speed, double totalGB, TypeRAM type) {
        this.speed = speed;
        this.totalGB = totalGB;
        this.type = type;
    }


    public static OperationResult<RAM> create(int speed, double totalGB, TypeRAM type) {
        if (speed <= 0) {
            return OperationResult.fail("Частота ОП должна быть положительной.");
        }
        if (totalGB <= 0) {
            return OperationResult.fail("Объем ОП должен быть положительным.");
        }
        if (type == null) {
            return OperationResult.fail("Тип ОП не может быть null.");
        }
        RAM ram = new RAM(speed, totalGB, type);
        return OperationResult.ok(ram, "RAM успешно создано.");
    }

    public OperationResult<Void> allocate(double allocateGB) {
        if (allocateGB < 0) {
            return OperationResult.fail("Чтобы зарезервировать место в ОП надо ввести положительное double число GB, которое хотите занять.");
        }
        if (usageGB + allocateGB > totalGB) {
            this.usageGB = totalGB;
        } else {
            this.usageGB += allocateGB;
        }
        return OperationResult.ok("Память успешно зарезервирована! Текущая занятая память составляет : " + usageGB + "Gb");
    }

    public OperationResult<Void> free(double freeGB) {
        if (freeGB < 0) {
            freeGB *= -1;
        }
        if (usageGB - freeGB < 0) {
            this.usageGB = 0;
        } else {
            this.usageGB -= freeGB;
        }
        return OperationResult.ok("Память успешно освобождена! Текущая занятая память составляет : " + usageGB + "Gb");
    }

    public OperationResult<Void> checkStatus() {
        double percent = (usageGB / totalGB) * 100.0;
        if (percent >= 85.0) {
            return OperationResult.ok("Состояние ОП | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Заполнение ОП на " + percent + "%\n");
        }else if (percent >= 70.0) {
            return OperationResult.ok("Состояние ОП | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Заполнение ОП на " + percent + "%\n");
        }
        return OperationResult.ok("Состояние ОП | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Заполнение ОП на " + percent + "%\n");
    }

    public OperationResult<Void> printInfo() {
        return OperationResult.ok("RAM{" +
                "speed=" + speed +
                ", totalGB=" + totalGB +
                ", usageGB=" + usageGB +
                ", type=" + type +
                '}');
    }
}
