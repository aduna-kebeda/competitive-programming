class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelvin, farh;
        kelvin=celsius + 273.15;
        farh=celsius * 1.80 + 32.00;
        vector<double>ans;
        ans.push_back(kelvin);
        ans.push_back(farh);
        return ans;
    }
};