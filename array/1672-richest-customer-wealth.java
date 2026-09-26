class Solution {
    public int maximumWealth(int[][] accounts) {
      int maximumWealthSoFar = 0;

      for (int[] customer: accounts) {
        int currentCustomerWealth = 0;

        for (int bank: customer) {
          currentCustomerWealth += bank;
        }

        maximumWealthSoFar = Math.max(maximumWealthSoFar, currentCustomerWealth);
      }

      return maximumWealthSoFar;
    }
}
