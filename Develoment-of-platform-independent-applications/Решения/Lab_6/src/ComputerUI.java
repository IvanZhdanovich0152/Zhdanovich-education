import java.util.Scanner;

public class ComputerUI {
    private final Scanner scanner;
    private Computer computer;

    public ComputerUI(Scanner scanner) {
        this.scanner = scanner;
    }

    public void start() {
        boolean running = true;
        while (running) {
            if (computer == null) {
                printBuildMenu();
                int choice = readInt("Выберите пункт: ", 0, 1);
                if (choice == 1) {
                    computer = build();
                    System.out.println("[УСПЕХ] -> Компьютер собран.");
                } else {
                    running = false;
                }
            } else {
                printMenu();
                int choice = readInt("Выберите пункт: ", 0, 8);
                switch (choice) {
                    case 1 -> printResponse(computer.turnOn());
                    case 2 -> printResponse(computer.turnoff());
                    case 3 -> handleRamMenu();
                    case 4 -> handleDiskMenu();
                    case 5 -> handleProcessorMenu();
                    case 6 -> handleReplaceMenu();
                    case 7 -> printResponse(computer.showSystemInfo());
                    case 8 -> printResponse(computer.checkSystemStatus());
                    case 0 -> running = false;
                }
            }
        }
        System.out.println("Программа завершена.");
    }

    private void printBuildMenu() {
        System.out.println("\n--- СБОРКА КОМПЬЮТЕРА ---");
        System.out.println("1. Собрать компьютер");
        System.out.println("0. Выход");
    }

    private void printMenu() {
        System.out.println("\n--- УПРАВЛЕНИЕ КОМПЬЮТЕРОМ ---");
        System.out.println("1. Включить компьютер");
        System.out.println("2. Выключить компьютер");
        System.out.println("3. Управление ОП");
        System.out.println("4. Управление диском");
        System.out.println("5. Управление процессором");
        System.out.println("6. Замена комплектующих");
        System.out.println("7. Показать информацию о системе");
        System.out.println("8. Проверить состояние системы");
        System.out.println("0. Выход");
    }

    private void handleRamMenu() {
        boolean running = true;
        while (running) {
            System.out.println("\n--- УПРАВЛЕНИЕ ОП ---");
            System.out.println("1. Выделить память");
            System.out.println("2. Освободить память");
            System.out.println("0. Назад");
            int choice = readInt("Выберите пункт: ", 0, 2);

            switch (choice) {
                case 1 -> printResponse(computer.allocateRAM(readDouble("Введите объем памяти в ГБ: ")));
                case 2 -> printResponse(computer.freeRAM(readDouble("Введите объем памяти в ГБ: ")));
                case 0 -> running = false;
            }
        }
    }

    private void handleDiskMenu() {
        boolean running = true;
        while (running) {
            System.out.println("\n--- УПРАВЛЕНИЕ ДИСКОМ ---");
            System.out.println("1. Записать данные");
            System.out.println("2. Удалить данные");
            System.out.println("0. Назад");
            int choice = readInt("Выберите пункт: ", 0, 2);

            switch (choice) {
                case 1 -> printResponse(computer.writeDisk(readDouble("Введите объем данных в ГБ: ")));
                case 2 -> printResponse(computer.deleteDisk(readDouble("Введите объем данных в ГБ: ")));
                case 0 -> running = false;
            }
        }
    }

    private void handleProcessorMenu() {
        boolean running = true;
        while (running) {
            System.out.println("\n--- УПРАВЛЕНИЕ ПРОЦЕССОРОМ ---");
            System.out.println("1. Установить нагрузку");
            System.out.println("0. Назад");
            int choice = readInt("Выберите пункт: ", 0, 1);

            switch (choice) {
                case 1 ->
                        printResponse(computer.setProcessorUsage(
                                readInt("Введите нагрузку процессора в процентах: ", 0, 100)));

                case 0 -> running = false;
            }
        }
    }

    private void handleReplaceMenu() {
        boolean running = true;
        while (running) {
            System.out.println("\n--- ЗАМЕНА КОМПЛЕКТУЮЩИХ ---");
            System.out.println("1. Заменить процессор");
            System.out.println("2. Заменить ОП");
            System.out.println("3. Заменить диск");
            System.out.println("0. Назад");
            int choice = readInt("Выберите пункт: ", 0, 3);

            switch (choice) {
                case 1 -> replaceProcessor();
                case 2 -> replaceRam();
                case 3 -> replaceDisk();
                case 0 -> running = false;
            }
        }
    }

    private Computer build() {
        System.out.println("\n--- СБОРКА КОМПЬЮТЕРА ---");
        System.out.println("Сначала задайте параметры всех комплектующих.");
        Processor processor = buildProcessor();
        RAM ram = buildRam();
        HardDisk disk = buildDisk();

        OperationResult<Computer> result = Computer.create(processor, ram, disk);
        if (result.isSuccess()) {
            printResponse(result);
            return result.value();
        } else {
            printResponse(result);
            return null;
        }

    }

    private Processor buildProcessor() {
        while (true) {
            System.out.println("\n--- ПРОЦЕССОР ---");
            String model = readString("Введите модель процессора: ");
            double speed = readDouble("Введите частоту процессора в ГГц: ");
            int cores = readInt("Введите количество ядер: ", 1, Integer.MAX_VALUE);
            int temperature = readInt("Введите температуру процессора: ", 0, Integer.MAX_VALUE);

            OperationResult<Processor> result = Processor.create(model, speed, cores, temperature);
            if (result.isSuccess()) {
                printResponse(result);
                return result.value();
            }
            printResponse(result);
            System.out.println("Повторите ввод параметров процессора.");

        }
    }

    private RAM buildRam() {
        while (true) {
            System.out.println("\n--- ОП ---");
            int speed = readInt("Введите частоту ОП в МГц: ", 1, Integer.MAX_VALUE);
            double totalGB = readDouble("Введите общий объем ОП в ГБ: ");
            RAM.TypeRAM type = readRamType();

            OperationResult<RAM> result = RAM.create(speed, totalGB, type);
            if (result.isSuccess()) {
                printResponse(result);
                return result.value();
            }
            printResponse(result);
            System.out.println("Повторите ввод параметров ОП.");
        }
    }

    private HardDisk buildDisk() {
        while (true) {
            System.out.println("\n--- ДИСК ---");
            double totalGB = readDouble("Введите общий объем диска в ГБ: ");
            double usageGB = readDouble("Введите занятый объем диска в ГБ: ");
            HardDisk.TypeHardDisk type = readDiskType();

            OperationResult<HardDisk> result = HardDisk.create(totalGB, usageGB, type);
            if (result.isSuccess()) {
                printResponse(result);
                return result.value();
            }
            printResponse(result);
            System.out.println("Повторите ввод параметров диска.");
        }
    }

    private void replaceProcessor() {
        printResponse(computer.setProcessor(buildProcessor()));
    }

    private void replaceRam() {
        printResponse(computer.setRam(buildRam()));
    }

    private void replaceDisk() {
        printResponse(computer.setDisk(buildDisk()));
    }

    //

    private void printResponse(OperationResult<?> result) {
        System.out.println(result.isSuccess() ? "[УСПЕХ] -> " + result.message() : "[ОШИБКА] -> " + result.message());
    }

    //

    private int readInt(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            try {
                int value = Integer.parseInt(scanner.nextLine().trim());
                if (value >= min && value <= max) {
                    return value;
                }
            } catch (NumberFormatException ignored) {
            }
            System.out.println("Ошибка: введите целое число от " + min + " до " + max + ".");
        }
    }

    private double readDouble(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                double value = Double.parseDouble(scanner.nextLine().trim().replace(',', '.'));
                if (Double.isFinite(value) && value >= 0) {
                    return value;
                }
            } catch (NumberFormatException ignored) {
            }
            System.out.println("Ошибка: введите неотрицательное число.");
        }
    }
    private String readString(String prompt) {
        while (true) {
            System.out.print(prompt);
            String value = scanner.nextLine().trim();
            if (!value.isEmpty()) {
                return value;
            }
            System.out.println("Ошибка: значение не может быть пустым.");
        }
    }

    private RAM.TypeRAM readRamType() {
        System.out.println("Доступные типы ОП: DDR3, DDR4, DDR5");
        while (true) {
            try {
                return RAM.TypeRAM.valueOf(readString("Введите тип ОП: ").toUpperCase());
            } catch (IllegalArgumentException exception) {
                System.out.println("Ошибка: выберите DDR3, DDR4 или DDR5.");
            }
        }
    }

    private HardDisk.TypeHardDisk readDiskType() {
        System.out.println("Доступные типы дисков: HDD, SSD, NVME");
        while (true) {
            try {
                return HardDisk.TypeHardDisk.valueOf(readString("Введите тип диска: ").toUpperCase());
            } catch (IllegalArgumentException exception) {
                System.out.println("Ошибка: выберите HDD, SSD или NVME.");
            }
        }
    }
}
