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

    public String allocateRAM(double amount) {
        if (powerOn) {
            ram.allocate(amount);
            return "В ОП зарезервированно " + amount + "Гб";
        }
        return "Для начала надо включить компьютер";
    }

    public String freeRAM(double amount) {
        if (powerOn) {
            ram.free(amount);
            return "В ОП освобождено" + amount + "Гб";
        }
        return "Для начала надо включить компьютер";
    }

    public String writeDisk(double amount) {
        if (powerOn) {
            disk.write(amount);
            return "На диск записано " + amount + "Гб";
        }
        return "Для начала надо включить компьютер";
    }

    public String deleteDisk(double amount) {
        if (powerOn) {
            disk.delete(amount);
            return "С диска удалено" + amount + "Гб";
        }
        return "Для начала надо включить компьютер";
    }

    public String setProcessorUsage(int usage) {
        if (powerOn) {
            processor.setUsage(usage);
            return "Нагрузка установлена на " + usage;
        }
        return "Для начала надо включить компьютер";
    }


    public void setProcessor(Processor processor) {
        this.processor = processor;
    }

    public void setRam(RAM ram) {
        this.ram = ram;
    }

    public void setDisk(HardDisk disk) {
        this.disk = disk;
    }


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
