public class Processor {
    private final String model;
    private final double speed;
    private final int cores;
    private final int temperature;
    private int usage;

    private Processor(String model, double speed, int cores, int temperature) {
        this.model = model;
        this.speed = speed;
        this.cores = cores;
        this.temperature = temperature;
    }

    public static OperationResult<Processor> create(String model, double speed, int cores, int temperature) {
        if (model == null) {
            return OperationResult.fail("Модель процессора не может быть пустой.");
        }
        if (speed <= 0) {
            return OperationResult.fail("Частота процессора должна быть положительной.");
        }
        if (cores <= 0) {
            return OperationResult.fail("Количество ядер должно быть положительным.");
        }
        if (temperature < 0) {
            return OperationResult.fail("Температура не может быть отрицательной.");
        }
        Processor processor = new Processor(model, speed, cores, temperature);
        return OperationResult.ok(processor, "Процессор успешно создан");
    }



    public OperationResult<Void> setUsage(int usage) {
        if (usage < 0 ) {
            this.usage = Math.max(0, this.usage - usage);
            return OperationResult.ok("Загруженность процессора уменьшена до :" + this.usage + "%");
        } else {
            this.usage = Math.min(100, usage);
            return OperationResult.ok("Загруженность процессора изменена на :" + this.usage + "%");
        }
    }

    public OperationResult<Void> checkStatus() {
        String result = "";
        if (temperature > 100) {
            result += "Температура процессора | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Критическое значение температуры процессора : " + temperature + "C\n";
        }else if (temperature > 85) {
            result += "Температура процессора | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Температура процессора выше нормы : " + temperature + "C\n";
        } else {
            result += "Температура процессора | " +
                    Computer.TypeComponentStatus.NORMAL +
                    " | Температура процессора в норме : " + temperature + "C\n";
        }
        if (usage > 90) {
            result += "Загруженность процессора | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Критическое значение загруженности процессора : " + usage + "%\n";
        }else if (usage > 75) {
            result += "Заруженность процессора | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Загруженность процессора выше нормы : " + usage + "%\n";
        }
        result += "Загруженность процессора | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Загруженность процессора в норме : " + usage + "%\n";

        return OperationResult.ok(result);
    }

    public OperationResult<Void> printInfo() {
        return OperationResult.ok("Processor{" +
                "model='" + model + '\'' +
                ", speed=" + speed +
                ", cores=" + cores +
                ", temperature=" + temperature +
                ", usage=" + usage +
                '}');
    }
}
