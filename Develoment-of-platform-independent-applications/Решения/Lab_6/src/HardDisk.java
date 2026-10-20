public class HardDisk {
    public enum TypeHardDisk {HDD, SSD, NVME}

    private double totalGB;
    private double usageGB;
    private TypeHardDisk type;


    public HardDisk() {
        this(2048, 1235.43, TypeHardDisk.HDD);
    }

    public HardDisk(double totalGB, double usageGB, TypeHardDisk type) {
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
        }
        return "Данные успешно записаны! Текущая заполненность диска : " + usageGB + "Gb";
    }

    public String delete(double freeGB) {
        if (freeGB < 0) {
            freeGB *= -1;
        }
        if (usageGB - freeGB < 0) {
            this.usageGB = 0;
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
