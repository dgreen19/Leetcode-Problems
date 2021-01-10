class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> output_arr = new ArrayList();
        for (int i = 1, fizz = 0, buzz = 0; i <= n; i++) {
            fizz++; //Increments by 1 each time loop is iterated
            buzz++; //Increments by 1 each time loop is iterated
            if (fizz == 3 && buzz ==5) {
                fizz = 0; //resets back to 0 once multiple is confirmed
                buzz = 0; //resets back to 0 once multiple is confirmed
                output_arr.add("FizzBuzz"); //prints FizzBuzz
            } else if (fizz == 3) {
                //checks for if fizz is mutiple of 3
                fizz = 0; //resets back to 0 once multiple is confirmed
                output_arr.add("Fizz");
                
            } else if (buzz == 5) {
                //checks for if buzz is multiple of 5
                buzz = 0; //resets back to 0 once multiple is confirmed
                output_arr.add("Buzz");
            } else {
                output_arr.add(Integer.toString(i));
            }
        }
        return output_arr;
    }
}
