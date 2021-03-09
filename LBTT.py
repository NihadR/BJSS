calculated = {}
def LBTT_calculator(n):
    levels = 3
    threshold = {250000, 325000, 750000}
    rate = {0.05, 0.1, 0.12}

    tax = 0
    


double netIncome = 55000;

        int levels = 3;
        double[] threshold = {0, 15000, 29000, 50000};
        double[] rate = {0, 15,20,25};

        double taxOwd = 0;

        double taxableIncome = 0;
        double netIncomeLeft = netIncome;

        for (int i = levels; i > 0; i--) {
            taxableIncome = netIncomeLeft - threshold[i];
            taxOwd += taxableIncome * (rate[i]/100);
            netIncomeLeft = threshold[i];
        }
        System.out.println("taxOwd " + taxOwd);

        
LBTT_calculator(1100000)