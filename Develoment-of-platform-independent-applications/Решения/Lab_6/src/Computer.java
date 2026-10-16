public class Computer {
    private Processor processor;
    private RAM ram;
    private HardDisk disk;
    private boolean powerOn;

    public Computer(Processor processor, RAM ram, HardDisk disk) {
        this.processor = processor;
        this.ram = ram;
        this.disk = disk;
    }

    public Computer() {
        this(
                new Processor(),
                new RAM(),
                new HardDisk()
        );
    }
}
