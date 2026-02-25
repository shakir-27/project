public class ViolationsExample {
    
    int publicField;
    
    public void methodWithTooManyParams(int a, int b, int c, int d, int e, int f, int g) {
        if (a > 42) {
            System.out.println("Too many params");
        }
        
        if (b < 10)
            System.out.println("No braces");
        
        if (c > 0) {
            return;
        } else {
            return;
        }
        
        logger("Error occurred");
        logger("Error occurred");
    }
    
    private void unusedMethod() {
        System.out.println("Unused");
    }
    
    public int badSwitch(int x) {
        switch (x) {
            case 1:
            case 2:
                return 10;
            default:
                return 0;
        }
    }
    
    public void badIteration() {
        java.util.List<String> list = new java.util.ArrayList<>();
        list.add("a");
        list.add("b");
        for (String s : list) {
            if (s.equals("a")) {
                list.remove(s);
            }
        }
    }
    
    public static void main(String[] args) {
        System.out.println("This line is intentionally over 100 characters long to demonstrate line length violation......................");
        
        ViolationsExample ex = new ViolationsExample();
        ex.methodWithTooManyParams(1,2,3,4,5,6,7);
    }
    
    private void logger(String msg) {
        System.out.println(msg);
    }
}

