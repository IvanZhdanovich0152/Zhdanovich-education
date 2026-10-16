public class Processor {
    private final String model;
    private final double speed;
    private final int cores;
    private final int temperature;
    private int usage;

    public Processor() {
        this("AMD Ryzen 5 5500", 4.2, 6, 50);
    }

    public Processor(String model, double speed, int cores, int temperature) {
        this.model = model;
        this.speed = speed;
        this.cores = cores;
        this.temperature = temperature;
    }

    public boolean checkHealth() {
        return this.temperature <= 100;
    }

    public void setUsage(int usage) {
        this.usage = usage;
    }

    @Override
    public String toString() {
        return "Processor{" +
                "model='" + model + '\'' +
                ", speed=" + speed +
                ", cores=" + cores +
                ", temperature=" + temperature +
                ", usage=" + usage +
                '}';
    }
}
