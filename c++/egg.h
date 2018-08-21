#include <string>

using namespace std;

class Egg{
public:
	Egg(double x_in, double y_in, double w_in, double h_in);
	~Egg();

	double x;
	double y;
	double w;
	double h;
	double area;
	double distance_to_center;
	double distance;

	double print();
};

int get_eggs_info(const string &filepath, Egg *eggs);
Egg get_nearest_egg(const Egg *eggs, const int &n_egg);
int same_target_egg(const Egg &egg, const Egg &last_egg);

def same_target_egg(egg, last_egg):
	if egg.y < last_egg.y:
		return False
	elif math.sqrt(4 * (egg.x - last_egg.x) ** 2 + 3 * (egg.y - last_egg.y) ** 2) > THRES_DIS_BETWEEN_EGG:
		return False
	else:
		return True