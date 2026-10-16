import java.util.Scanner;

public class WateringSystemUI {
    private final Scanner scanner;
    private SimpleWateringSystem system = null;

    public WateringSystemUI(Scanner scanner) {
        this.scanner = scanner;
    }

    public void start() {
        boolean isRunning = true;
        while (isRunning) {
            printMenu();
            int choice = readInt("Выберите пункт: ", 0, 5);
            if (system == null && choice > 1) {
                System.out.println("Ошибка: Сначала создайте систему полива почвы (пункт 1)!");
                continue;
            }
            switch (choice) {
                case 1 -> handleCreate();
                case 2 -> handleWater();
                case 3 -> handleFillTank();
                case 4 -> handleToggleWaterState();
                case 5 -> system.showStatus();
                case 0 -> isRunning = false;
            }
        }
        System.out.println("Программа завершена.");
    }

    private void printMenu() {
        System.out.println("\n--- УПРАВЛЕНИЕ ЧЕРЕЗ ИНТЕРФЕЙС ---");
        System.out.println("1. Создать систему полива почвы");
        System.out.println("2. Вызвать water (Начать полив)");
        System.out.println("3. Вызвать fillTank (Наполнение танка)");
        System.out.println("4. Вызвать toggleWaterState (переключение состояния полива)");
        System.out.println("5. Показать текущее состояние");
        System.out.println("0. Выход");
    }

    public void handleCreate() {
        int moistureLevel = readInt("Введите % влажности почвы: ", 0, 100);
        int MaxWaterTank = readInt("Введите максимальную вместимость бака: ", 100, 9999999);
        int waterTank = readInt("Введите кол-во воды в баке на данный момент: ", 0, MaxWaterTank);
        WateringSystem.WaterState waterState = getWaterState();

        OperationResult<WateringSystem> result = WateringSystem.create(-waterTank, MaxWaterTank, moistureLevel, waterState);

        if (result.isSuccess()) {
            this.system = result.value();
            printResponse(result);
        } else {
            printResponse(result);
        }
    }

    public void handleWater() {
        int durationMinutes = readInt("Введите количество минут полива: ", 1, 999999999);
        OperationResult<Void> result = system.water(durationMinutes);
        printResponse(result);
    }

    public void handleFillTank() {
        int liters = readInt("Введите количество литров, которое надо долить в бак: ", 1, 999999999);
        OperationResult<Void> result = system.fillTank(liters);
        printResponse(result);
    }

    public void handleToggleWaterState() {
        OperationResult<Void> result = system.toggleWaterState();
        printResponse(result);
    }

    private void printResponse(OperationResult<?> result) {
        System.out.println(result.isSuccess() ? "[УСПЕХ] -> " + result.message() : "[ОШИБКА] -> " + result.message());
    }

    private int readInt(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            if (scanner.hasNextInt()) {
                int value = scanner.nextInt();
                if (value >= min && value <= max) return value;
                System.out.println("Ошибка диапазона!");
            } else {
                System.out.println("Ошибка: введите целое число.");
                scanner.next();
            }
        }
    }

    private WateringSystem.WaterState getWaterState() {
        scanner.nextLine();
        System.out.print("Введите текущее состояние полива ( ");
        WateringSystem.WaterState[] wsv = WateringSystem.WaterState.values();
        for (WateringSystem.WaterState ws: wsv) {
            System.out.print(ws + " ");
        }
        System.out.print("): ");

        String userInput = scanner.nextLine();
        return WateringSystem.WaterState.valueOf(userInput.toUpperCase());
    }

}
