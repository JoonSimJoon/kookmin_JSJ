
public class Lec04Util {

  // print a binary string for a given number of type byte, short, int, or long
  public static String toBinaryStringInFull(String s, String numType,
       boolean prettyView) {
	    int size = 0;

	    switch (numType) {
	      case ("java.lang.Byte"):
	        size = 8;
	        break;
	      case ("java.lang.Short"):
	        size = 16;
	        break;
	      case ("java.lang.Integer"):
	        size = 32;
	        break;
	      case ("java.lang.Long"):
	        size = 64;
	        break;
	      default:
	        System.out.println("Wrong type: must be byte, short, int or long type");
	        return null;
	    }

	    while (s.length() < size) {
	      s = "0" + s;
	    }

	    if (prettyView) { // put a blank per 8 bits and "_" per 4 bits
	      int ix = 0;

	      String s2 = "" + s.charAt(ix++);
	      while (ix < size) {
	        if (ix % 8 == 0) {
	          s2 = s2 + " " + s.charAt(ix);

	        } else if (ix % 4 == 0) {
	          s2 = s2 + "_" + s.charAt(ix);
	        } else
	          s2 = s2 + s.charAt(ix);
	        ix++;
	      }

	      s = s2;
	    }

	    return s;
  }

  // print a binary string for a given number of type byte, short, int, or long
  public static String toBinaryStringInFull(int num, boolean prettyView) {
	    int size = 0;
	    String s = Integer.toBinaryString(num);
	    String numType = ((Object) num).getClass().getName();

	    switch (numType) {
	      case ("java.lang.Byte"):
	        size = 8;
	        break;
	      case ("java.lang.Short"):
	        size = 16;
	        break;
	      case ("java.lang.Integer"):
	        size = 32;
	        break;
	      case ("java.lang.Long"):
	        size = 64;
	        break;
	      default:
	        System.out.println("Wrong type: must be byte, short, int or long type");
	        return null;
	    }

	    while (s.length() < size) {
	      s = "0" + s;
	    }

	    if (prettyView) { // put a blank per 8 bits and "_" per 4 bits
	      int ix = 0;

	      String s2 = "" + s.charAt(ix++);
	      while (ix < size) {
	        if (ix % 8 == 0) {
	          s2 = s2 + " " + s.charAt(ix);

	        } else if (ix % 4 == 0) {
	          s2 = s2 + "_" + s.charAt(ix);
	        } else
	          s2 = s2 + s.charAt(ix);
	        ix++;
	      }

	      s = s2;
	    }

	    return s;
  }

  public static void main(String[] args) {
    testToBinaryStringInFull();
    
    System.out.println(Lec04Util.toBinaryStringInFull(65, false));
    System.out.println(Lec04Util.toBinaryStringInFull(65, true));
  }

  private static void testToBinaryStringInFull1() {
    // Given an integer number 1, show results after 1 bit shift.
    int num = 1;
    for (int i = 0; i < 32; i++) {
      System.out.println(num);
      // print binary string in full
      System.out.println(Lec04Util.toBinaryStringInFull(Integer.toBinaryString(num),
          ((Object) i).getClass().getName(), false));
      // print binary string in full, with pretty format
      System.out.println(Lec04Util.toBinaryStringInFull(Integer.toBinaryString(num),
          ((Object) i).getClass().getName(), true));

      num = num << 1; // shift 1 bit left
    }
  }

  private static void testToBinaryStringInFull() {
	    // Given an integer number 1, show results after 1 bit shift.
	    int num = 1;
	    for (int i = 0; i < 32; i++) {
	      System.out.println(num);
	      // print binary string in full
	      System.out.println(Lec04Util.toBinaryStringInFull(num, false));
	      // print binary string in full, with pretty format
	      System.out.println(Lec04Util.toBinaryStringInFull(num, true));

	      num = num << 1; // shift 1 bit left
	    }
  }

}
