public class Computer {
    public enum TypeComponentStatus {NORMAL, WARNING, CRITICAL}
    private Processor processor;
    private RAM ram;
    private HardDisk disk;
    private boolean powerOn = false;

    public Computer(Processor processor, RAM ram, HardDisk disk) {
        if (processor == null) {
            throw new IllegalArgumentException("Процессор не может быть null.");
        }
        if (ram == null) {
            throw new IllegalArgumentException("ОП не может быть null.");
        }
        if (disk == null) {
            throw new IllegalArgumentException("Диск не может быть null.");
        }
        this.processor = processor;
        this.ram = ram;
        this.disk = disk;
    }

    public String turnOn() {
        ram.allocate(2.3);
        processor.setUsage(13);
        powerOn = true;
        return "Компьютер включен.";
    }

    public String turnoff() {
        ram.free(128.0);
        processor.setUsage(0);
        powerOn = false;
        return "Компьютер выключен.";
    }

    public boolean isPowerOn() {
        return powerOn;
    }

    public String allocateRAM(double amount) {
        if (powerOn) {
            return ram.allocate(amount);
        }
        return "Для начала надо включить компьютер";
    }

    public String freeRAM(double amount) {
        if (powerOn) {
            return ram.free(amount);
        }
        return "Для начала надо включить компьютер";
    }

    public String writeDisk(double amount) {
        if (powerOn) {
            return disk.write(amount);
        }
        return "Для начала надо включить компьютер";
    }

    public String deleteDisk(double amount) {
        if (powerOn) {
            return disk.delete(amount);
        }
        return "Для начала надо включить компьютер";
    }

    public String setProcessorUsage(int usage) {
        if (powerOn) {
            return processor.setUsage(usage);
        }
        return "Для начала надо включить компьютер";
    }


    public void setProcessor(Processor processor) {
        if (processor == null) {
            throw new IllegalArgumentException("Процессор не может быть null.");
        }
        this.processor = processor;
    }

    public void setRam(RAM ram) {
        if (ram == null) {
            throw new IllegalArgumentException("ОП не может быть null.");
        }
        this.ram = ram;
    }

    public void setDisk(HardDisk disk) {
        if (disk == null) {
            throw new IllegalArgumentException("Диск не может быть null.");
        }
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
