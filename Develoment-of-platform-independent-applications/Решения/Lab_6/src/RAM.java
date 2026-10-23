public class RAM {
    public enum TypeRAM {DDR3, DDR4, DDR5}

    private final int speed;
    private final double totalGB;
    private double usageGB = 0;
    private final TypeRAM type;

    public RAM(int speed, double totalGB, TypeRAM type) {
        if (speed <= 0) {
            throw new IllegalArgumentException("Частота ОП должна быть положительной.");
        }
        if (totalGB <= 0) {
            throw new IllegalArgumentException("Объем ОП должен быть положительным.");
        }
        if (type == null) {
            throw new IllegalArgumentException("Тип ОП не может быть null.");
        }
        this.speed = speed;
        this.totalGB = totalGB;
        this.type = type;
    }

    public String allocate(double allocateGB) {
        if (allocateGB < 0) {
            return "Чтобы зарезервировать место в ОП надо ввести положительное double число GB, которое хотите занять.";
        }
        if (usageGB + allocateGB > totalGB) {
            this.usageGB = totalGB;
        } else {
            this.usageGB += allocateGB;
        }
        return "Память успешно зарезервирована! Текущая занятая память составляет : " + usageGB + "Gb";
    }

    public String free(double freeGB) {
        if (freeGB < 0) {
            freeGB *= -1;
        }
        if (usageGB - freeGB < 0) {
            this.usageGB = 0;
        } else {
            this.usageGB -= freeGB;
        }
        return "Память успешно освобождена! Текущая занятая память составляет : " + usageGB + "Gb";
    }

    public String checkStatus() {
        double percent = (usageGB / totalGB) * 100.0;
        if (percent >= 85.0) {
            return "Состояние ОП | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Заполнение ОП на " + percent + "%\n";
        }else if (percent >= 70.0) {
            return "Состояние ОП | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Заполнение ОП на " + percent + "%\n";
        }
        return "Состояние ОП | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Заполнение ОП на " + percent + "%\n";
    }

    @Override
    public String toString() {
        return "RAM{" +
                "speed=" + speed +
                ", totalGB=" + totalGB +
                ", usageGB=" + usageGB +
                ", type=" + type +
                '}';
    }
}
