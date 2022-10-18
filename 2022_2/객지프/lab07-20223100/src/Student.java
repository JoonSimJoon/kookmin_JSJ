
public class Student {
	private String name;
	private int score;
	
	public Student(String name, int score) {
		this.name = name;
		this.score = score;
	}
	
	public void setName(String name_) {
		name = name_;
	}
	
	public String getName() {
		return name;
	}
		
	public void setScore(int score_) {
		score = score_;
	}
	
	public int getScore() {
		return score;
	}
}