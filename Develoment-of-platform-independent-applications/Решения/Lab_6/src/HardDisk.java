public class HardDisk {
    public enum TypeHardDisk {HDD, SSD, NVME}
    private final double totalGB;
    private double usageGB;
    private final TypeHardDisk type;

    private HardDisk(double totalGB, double usageGB, TypeHardDisk type) {
        this.totalGB = totalGB;
        this.usageGB = usageGB;
        this.type = type;
    }

    public static OperationResult<HardDisk> create(double totalGB, double usageGB, TypeHardDisk type){
        if (totalGB <= 0) {
            return OperationResult.fail("Объем диска должен быть положительным.");
        }
        if (usageGB < 0) {
            return OperationResult.fail("Занятый объем диска не может быть отрицательным.");
        }
        if (usageGB > totalGB) {
            return OperationResult.fail("Занятый объем не может быть больше общего объема диска.");
        }
        if (type == null) {
            return OperationResult.fail("Тип диска не может быть null.");
        }
        HardDisk disk = new HardDisk(totalGB, usageGB, type);
        return OperationResult.ok(disk, "Диск успешно создан");
    }

    public OperationResult<Void> write(double writeGB) {
        if (writeGB < 0) {
            return OperationResult.ok("Чтобы записать данные на диск надо ввести положительное double число GB, которое хотите занять.");
        }
        if (usageGB + writeGB > totalGB) {
            this.usageGB = totalGB;
        } else {
            this.usageGB += writeGB;
        }
        return OperationResult.ok("Данные успешно записаны! Текущая заполненность диска : " + usageGB + "Gb");
    }

    public OperationResult<Void> delete(double freeGB) {
        if (freeGB < 0) {
            freeGB *= -1;
        }
        if (usageGB - freeGB < 0) {
            this.usageGB = 0;
        } else {
            this.usageGB -= freeGB;
        }
        return OperationResult.ok("Данные успешно удалены! Текущая заполненность диска : " + usageGB + "Gb");
    }

    public OperationResult<Void> checkStatus() {
        double percent = (usageGB / totalGB) * 100.0;
        if (percent >= 85.0) {
            return OperationResult.ok("Состояние диска | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Заполнение диска на " + percent + "%\n");
        }else if (percent >= 70.0) {
            return OperationResult.ok("Состояние диска | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Заполнение диска на " + percent + "%\n");
        }
        return OperationResult.ok("Состояние диска | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Заполнение диска на " + percent + "%\n");
    }

    public OperationResult<Void> printInfo() {
        return OperationResult.ok("HardDisk{" +
                "totalGB=" + totalGB +
                ", usageGB=" + usageGB +
                ", type=" + type +
                '}');
    }
}
