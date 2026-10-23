public class HardDisk {
    public enum TypeHardDisk {HDD, SSD, NVME}
    private final double totalGB;
    private double usageGB;
    private final TypeHardDisk type;

    public HardDisk(double totalGB, double usageGB, TypeHardDisk type) {
        if (totalGB <= 0) {
            throw new IllegalArgumentException("Объем диска должен быть положительным.");
        }
        if (usageGB < 0) {
            throw new IllegalArgumentException("Занятый объем диска не может быть отрицательным.");
        }
        if (usageGB > totalGB) {
            throw new IllegalArgumentException("Занятый объем не может быть больше общего объема диска.");
        }
        if (type == null) {
            throw new IllegalArgumentException("Тип диска не может быть null.");
        }
        this.totalGB = totalGB;
        this.usageGB = usageGB;
        this.type = type;
    }

    public String write(double writeGB) {
        if (writeGB < 0) {
            return "Чтобы записать данные на диск надо ввести положительное double число GB, которое хотите занять.";
        }
        if (usageGB + writeGB > totalGB) {
            this.usageGB = totalGB;
        } else {
            this.usageGB += writeGB;
        }
        return "Данные успешно записаны! Текущая заполненность диска : " + usageGB + "Gb";
    }

    public String delete(double freeGB) {
        if (freeGB < 0) {
            freeGB *= -1;
        }
        if (usageGB - freeGB < 0) {
            this.usageGB = 0;
        } else {
            this.usageGB -= freeGB;
        }
        return "Данные успешно удалены! Текущая заполненность диска : " + usageGB + "Gb";
    }

    public String checkStatus() {
        double percent = (usageGB / totalGB) * 100.0;
        if (percent >= 85.0) {
            return "Состояние диска | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Заполнение диска на " + percent + "%\n";
        }else if (percent >= 70.0) {
            return "Состояние диска | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Заполнение диска на " + percent + "%\n";
        }
        return "Состояние диска | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Заполнение диска на " + percent + "%\n";
    }

    @Override
    public String toString() {
        return "HardDisk{" +
                "totalGB=" + totalGB +
                ", usageGB=" + usageGB +
                ", type=" + type +
                '}';
    }
}
