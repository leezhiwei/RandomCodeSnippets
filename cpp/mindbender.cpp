#include <iostream>
bool mindbender() {
    bool value = true;
    bool notvalue = false;
    if (value == true and notvalue != true and value != notvalue){
	return true;
}
    else if (notvalue == value) {
        return false;
}
    else{
        return notvalue;
}
}
int main() {
    if (mindbender() == true) {
        bool x = false;
        bool y = (x == mindbender());
        std::cout << "Bool is ";
        std::cout << std::boolalpha;
        std::cout << y << std::endl;
}
else{
    std::cout << "Pain is ";
    std::cout << std::boolalpha;
    std::cout << false << std::endl;
}
return 0;
}
