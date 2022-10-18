package kr.ac.kookmin.udclasses;

public class Order {
	private DVD dvdsOrdered[] = new DVD[10];
	private int numOrdered = 0;
	
	public int getNumOrdered() {
		return numOrdered;
	}
	
	public void setNumOrdered(int numOrdered) {
		this.numOrdered = numOrdered;
	}
	
	public void addDVD(DVD disc) {
		int qty = getNumOrdered();
		if (qty < 10) {
			dvdsOrdered[qty] = disc;
			setNumOrdered(qty+1);
		}
	}
	
	public void removeDVD(DVD disc) {
		int qty = getNumOrdered();
		if (qty > 0) {
			for (int i = 0; i < qty; i++) {
				if (disc.equals(dvdsOrdered[i])) {
					dvdsOrdered[i] = null;
					setNumOrdered(qty-1);
					break;
				}
			}
		}
	}
	
	public float totalCost() {
		int num = getNumOrdered();
		float total = 0;
		for (int i = 0; i < num; i++) {
			total = total + dvdsOrdered[i].getCost();
		}
		return total;
	}
	
	
}
