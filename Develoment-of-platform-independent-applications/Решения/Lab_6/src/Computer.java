public class Computer {
    public enum TypeComponentStatus {NORMAL, WARNING, CRITICAL}
    private Processor processor;
    private RAM ram;
    private HardDisk disk;
    private boolean powerOn = false;

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

    public void turnOn() {
        ram.allocate(2.3);
        processor.setUsage(13);
        powerOn = true;
    }

    public void turnoff() {
        ram.free(128.0);
        processor.setUsage(0);
        powerOn = false;
    }

    public boolean isPowerOn() {
        return powerOn;
    }

    // Методы работы с памятью ram.allocate()/.free()
    // Методы работы с память disk.write()/.delete()
    // Метод для работы с нагрузкой ЦП processor.setUsage()

    // Добавить сеттеры для цп оп и вп








    public String checkSystemStatus(){
        if (powerOn) {
            return processor.checkStatus() + ram.checkStatus() + disk.checkStatus();
        }
        return "Для начала надо включить компьютер";
    }

    public String showSystemInfo() {
        if (powerOn) {
            return processor + "\n" + ram + "\n" + disk;
        }
        return "Для начала надо включить компьютер";
    }
}
