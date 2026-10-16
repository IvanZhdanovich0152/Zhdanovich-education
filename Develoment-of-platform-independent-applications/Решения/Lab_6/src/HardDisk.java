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

    public void write(double usageGB) {
        this.usageGB += usageGB;
    }

    public void delete(double freeGB) {
        this.usageGB -= freeGB;
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
