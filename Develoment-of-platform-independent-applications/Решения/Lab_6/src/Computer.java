public class Computer {
    public enum TypeComponentStatus {NORMAL, WARNING, CRITICAL}
    private Processor processor;
    private RAM ram;
    private HardDisk disk;
    private boolean powerOn = false;

    private Computer(Processor processor, RAM ram, HardDisk disk) {
        this.processor = processor;
        this.ram = ram;
        this.disk = disk;
    }

    public static OperationResult<Computer> create(Processor processor, RAM ram, HardDisk disk) {
        if (processor == null) {
            return OperationResult.fail("Процессор не может быть null.");
        }
        if (ram == null) {
            return OperationResult.fail("ОП не может быть null.");
        }
        if (disk == null) {
            return OperationResult.fail("Диск не может быть null.");
        }
        Computer computer = new Computer(processor, ram, disk);
        return OperationResult.ok(computer, "Компьютер успешно создан");
    }

    public OperationResult<Void> turnOn() {
        ram.allocate(2.3);
        processor.setUsage(13);
        powerOn = true;
        return OperationResult.ok("Компьютер включен.");
    }

    public OperationResult<Void> turnoff() {
        ram.free(128.0);
        processor.setUsage(0);
        powerOn = false;
        return OperationResult.ok("Компьютер выключен.");
    }

    public OperationResult<Void> allocateRAM(double amount) {
        if (powerOn) {
            return ram.allocate(amount);
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }

    public OperationResult<Void> freeRAM(double amount) {
        if (powerOn) {
            return ram.free(amount);
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }

    public OperationResult<Void> writeDisk(double amount) {
        if (powerOn) {
            return disk.write(amount);
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }

    public OperationResult<Void> deleteDisk(double amount) {
        if (powerOn) {
            return disk.delete(amount);
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }

    public OperationResult<Void> setProcessorUsage(int usage) {
        if (powerOn) {
            return processor.setUsage(usage);
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }


    public OperationResult<Void> setProcessor(Processor processor) {
        if (processor == null) {
            return OperationResult.fail("Процессор не может быть null.");
        }
        this.processor = processor;
        return OperationResult.ok("Процессор успешно заменён.");
    }

    public OperationResult<Void> setRam(RAM ram) {
        if (ram == null) {
            return OperationResult.fail("ОП не может быть null.");
        }
        this.ram = ram;
        return OperationResult.ok("ОП успешно заменено.");
    }

    public OperationResult<Void> setDisk(HardDisk disk) {
        if (disk == null) {
            return OperationResult.fail("Диск не может быть null.");
        }
        this.disk = disk;
        return OperationResult.ok("Диск успешно заменён.");
    }


    public OperationResult<Void> checkSystemStatus(){
        if (powerOn) {
            return OperationResult.ok(
                            processor.checkStatus().message() +
                            ram.checkStatus().message() +
                            disk.checkStatus().message());
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }

    public OperationResult<Void> showSystemInfo() {
        if (powerOn) {
            return OperationResult.ok(
                            processor.printInfo().message() + "\n" +
                            ram.printInfo().message() + "\n" +
                            disk.printInfo().message()
            );
        }
        return OperationResult.fail("Для начала надо включить компьютер");
    }
}
