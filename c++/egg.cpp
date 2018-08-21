#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

#include "egg.h"

using namespace std;

Egg::Egg(double x_in, double y_in, double w_in, double h_in) {
	x = x_in;
	y = y_in;
	w = w_in;
	h = w_in;

	area = w * h;
	distance_to_center = sqrt(4 * pow((x - 0.5), 2) + 3 * pow((y - 0.5), 2));
	distance = sqrt(area) + distance_to_center + 0;
}

int Egg::get_eggs_info(const string &filepath, Egg *eggs) {
	
}

Egg Egg::get_nearest_egg(const Egg *eggs, const int &n_egg) {

}

int Egg::same_target_egg(const Egg &egg, const Egg &last_egg) {
	
}