public record OperationResult<T>(boolean isSuccess, String message, T value) {

    public static <T> OperationResult<T> ok(T value, String message) {
        return new OperationResult<>(true, message, value);
    }

    public static OperationResult<Void> ok(String message) {
        return new OperationResult<>(true, message, null);
    }

    public static <T> OperationResult<T> fail(String message) {
        return new OperationResult<>(false, message, null);
    }
}