import java.util.Scanner;

public class Main {
    private static final int MAX_GATES = 10;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GateController[] gates = new GateController[MAX_GATES];
        boolean running = true;

        while (running) {
            printMenu();
            int command = readInt(scanner, "Выберите пункт: ");
            switch (command) {
                case 1 -> createGate(scanner, gates);
                case 2 -> openAll(gates);
                case 3 -> specificAction(scanner, gates);
                case 4 -> modifyGate(scanner, gates);
                case 5 -> printGates(gates);
                case 0 -> running = false;
                default -> System.out.println("Неизвестный пункт меню.");
            }
        }
        System.out.println("Программа завершена.");
    }

    private static void printMenu() {
        System.out.println("\n1. Создать объект");
        System.out.println("2. Выполнить открытие всех объектов");
        System.out.println("3. Специфическое действие");
        System.out.println("4. Изменить состояние объекта");
        System.out.println("5. Показать объекты");
        System.out.println("0. Выход");
    }

    private static void createGate(Scanner scanner, GateController[] gates) {
        int index = firstFreeIndex(gates);
        if (index < 0) {
            System.out.println("Массив объектов заполнен.");
            return;
        }

        int type = readInt(scanner, "Тип (1-шлагбаум, 2-откатные, 3-рулонные): ");
        int checkpoint = readInt(scanner, "Номер КПП: ");
        boolean operating = readInt(scanner, "Электропривод (1-вкл, 0-выкл): ") == 1;
        GateController.TypeLockState lockState = readInt(scanner, "Шлюз (1-закрыт, 2-открыт): ") == 2
                ? GateController.TypeLockState.UNLOCKED
                : GateController.TypeLockState.ARMED_BLOCK;

        if (type == 1) {
            int angle = readInt(scanner, "Угол стрелы (0-90): ");
            int ledCode = readInt(scanner, "LED (1-зелёный, 2-красный, 3-выкл): ");
            ParkingBarrier.TypeStateLED led = ledCode == 1
                    ? ParkingBarrier.TypeStateLED.GREEN
                    : ledCode == 2
                    ? ParkingBarrier.TypeStateLED.RED
                    : ParkingBarrier.TypeStateLED.OFF;
            OperationResult<ParkingBarrier> result = ParkingBarrier.create(
                    checkpoint, operating, lockState, angle, led);
            if (!result.isSuccess()) {
                printUserAction(result.message());
                return;
            }
            gates[index] = result.value();
        } else if (type == 2) {
            int position = readInt(scanner, "Положение створки (0-100%): ");
            int tension = readInt(scanner, "Натяжение ремня: ");
            OperationResult<SlidingGate> result = SlidingGate.create(
                    checkpoint, operating, lockState, position, tension);
            if (!result.isSuccess()) {
                printUserAction(result.message());
                return;
            }
            gates[index] = result.value();
        } else if (type == 3) {
            int pressure = readInt(scanner, "Давление пневматической кромки: ");
            int wear = readInt(scanner, "Износ ПВХ-полотна (0-100%): ");
            OperationResult<HighSpeedRollGate> result = HighSpeedRollGate.create(
                    checkpoint, operating, lockState, pressure, wear);
            if (!result.isSuccess()) {
                printUserAction(result.message());
                return;
            }
            gates[index] = result.value();
        } else {
            printUserAction("Неизвестный тип объекта.");
            return;
        }
        System.out.println("Объект создан под индексом " + index + ".");
    }

    private static void openAll(GateController[] gates) {
        for (int i = 0; i < gates.length; i++) {
            if (gates[i] != null) {
                printResult(i, gates[i].startOpening());
            }
        }
    }

    private static void specificAction(Scanner scanner, GateController[] gates) {
        int index = readIndex(scanner, gates);
        if (index < 0) return;
        GateController gate = gates[index];
        OperationResult<Void> result;
        if (gate instanceof ParkingBarrier barrier) {
            result = barrier.detachBoomArm();
        } else if (gate instanceof SlidingGate slidingGate) {
            result = slidingGate.checkLimitSwitches();
        } else {
            result = ((HighSpeedRollGate) gate).heatRollMechanism();
        }
        printResult(index, result);
    }

    private static void modifyGate(Scanner scanner, GateController[] gates) {
        int index = readIndex(scanner, gates);
        if (index < 0) return;
        GateController gate = gates[index];
        int action = readInt(scanner, "1-включить привод, 2-выключить, 3-уникальная настройка: ");
        OperationResult<Void> result;
        if (action == 1 || action == 2) {
            result = gate.setOperating(action == 1);
        } else if (action == 3 ) {
            result = gate.modifyGate(readInt(scanner, "Введите новое значение: "));
        } else {
            result = OperationResult.fail("Недопустимое действие.");
        }
        printResult(index, result);
    }

    private static void printGates(GateController[] gates) {
        for (int i = 0; i < gates.length; i++) {
            if (gates[i] != null) {
                System.out.println("\n[" + i + "] " + gates[i]);
            }
        }
    }

    private static int readIndex(Scanner scanner, GateController[] gates) {
        int index = readInt(scanner, "Индекс объекта: ");
        if (index < 0 || index >= gates.length || gates[index] == null) {
            System.out.println("Объект с таким индексом отсутствует.");
            return -1;
        }
        return index;
    }

    private static int firstFreeIndex(GateController[] gates) {
        for (int i = 0; i < gates.length; i++) {
            if (gates[i] == null) return i;
        }
        return -1;
    }

    private static int readInt(Scanner scanner, String message) {
        System.out.print(message);
        String value = scanner.nextLine();
        try {
            return Integer.parseInt(value.trim());
        } catch (NumberFormatException exception) {
            System.out.println("Некорректное число, использовано значение 0.");
            return 0;
        }
    }

    private static void printResult(int index, OperationResult<Void> result) {
        if (result == null) {
            throw new IllegalStateException("Операция объекта вернула пустой результат.");
        }
        if (result.isSuccess()) {
            System.out.println("[" + index + "] " + result.message());
        } else {
            printUserAction("[" + index + "] " + result.message());
        }
    }

    private static void printUserAction(String message) {
        System.out.println(message);
        System.out.println("Действие не выполнено. Исправьте параметры или повторите операцию через меню.");
    }
}
