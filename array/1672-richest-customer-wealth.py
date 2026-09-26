class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximumWealthSoFar = 0

        for customer in accounts:
            currentCustomerWealth = 0

            for bank in customer:
                currentCustomerWealth += bank
            
            maximumWealthSoFar = max(maximumWealthSoFar, currentCustomerWealth)

        return maximumWealthSoFar
