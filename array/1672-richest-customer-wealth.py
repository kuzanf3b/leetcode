class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximumWealthSoFar = 0

        for customer in accounts:
            currentCustomerWealth = 0

            for bank in customer:
                currentCustomerWealth += bank
            
            maximumWealthSoFar = max(maximumWealthSoFar, currentCustomerWealth)

        return maximumWealthSoFar

    # time complexity: O(n * m) where n is the number of customers and m is the number of banks
    # space complexity: O(1) since we are using a constant amount of space
