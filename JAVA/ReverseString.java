public class ReverseString {
	
	public String reverseStringRecursively(String a){
		if((a == null) || (a.length()<=1)){
			return a;
		}
		return reverseStringRecursively(a.substring(1))+a.charAt(0);
	}

	public static void main(String[] args) {

		ReverseString reverseString = new ReverseString();
		System.out.println(reverseString.reverseStringRecursively("Team Avengers"));
	}

}
