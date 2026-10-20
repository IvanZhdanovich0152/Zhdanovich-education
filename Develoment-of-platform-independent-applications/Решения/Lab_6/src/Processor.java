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

    public String setUsage(int usage) {
        if (usage < 0 ) {
            this.usage = Math.max(0, this.usage - usage);
            return "Загруженность процессора уменьшена до :" + this.usage + "%";
        } else {
            this.usage = Math.min(100, usage);
            return "Загруженность процессора изменена на :" + this.usage + "%";
        }
    }

    public String checkStatus() {
        String status = "";
        if (temperature > 100) {
            status += "Температура процессора | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Критическое значение температуры процессора : " + temperature + "C\n";
        }else if (temperature > 85) {
            status += "Температура процессора | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Температура процессора выше нормы : " + temperature + "C\n";
        }
        status += "Температура процессора | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Температура процессора в норме : " + temperature + "C\n";
        if (usage > 90) {
            status += "Загруженность процессора | " +
                    Computer.TypeComponentStatus.CRITICAL +
                    " | Критическое значение загруженности процессора : " + usage + "%\n";
        }else if (usage > 75) {
            status += "Заруженность процессора | " +
                    Computer.TypeComponentStatus.WARNING +
                    " | Загруженность процессора выше нормы : " + usage + "%\n";
        }
        status += "Загруженность процессора | " +
                Computer.TypeComponentStatus.NORMAL +
                " | Загруженность процессора в норме : " + usage + "%\n";

        return status;
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
