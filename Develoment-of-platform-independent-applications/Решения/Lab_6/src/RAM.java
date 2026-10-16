public class RAM {
    public enum TypeRAM {DDR3, DDR4, DDR5}

    private int speed;
    private double totalGB;
    private double usageGB;
    private TypeRAM type;

    public RAM() {
        this(6000, 32.0, 3.2, TypeRAM.DDR5);
    }

    public RAM(int speed, double totalGB, double usageGB, TypeRAM type) {
        this.speed = speed;
        this.totalGB = totalGB;
        this.usageGB = usageGB;
        this.type = type;
    }

    public void allocate(double usageGB) {
        this.usageGB += usageGB;
    }

    public void free(double freeGB) {
        this.usageGB -= freeGB;
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
