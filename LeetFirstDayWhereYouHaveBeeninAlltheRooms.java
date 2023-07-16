class Solution {
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        // The highest room number that needs to be visited
        int maxRoomNum = nextVisit.length;
        // Stores the number of visits of each room
        int[] pre = new int[maxRoomNum];
        // The maximum number of days that is possible
        int m = (int) 1e9 + 7;
        for (int i = 1; i < maxRoomNum; i++) {
            // pre[i] means the first time we enter the room i
            // To get to the room i, we need to visit the previous room at least twice. Thus we have pre[i-1] + 1+ ...
            // Another way to visit room i is to go back from higher numbered rooms to the previous room before i
            // Thus we have pre[i-1] - pre[nextVisit[i-1]]
            pre[i] = (pre[i-1]+1+(pre[i-1] - pre[nextVisit[i-1]] + m) % m + 1) %m;
        }
        return pre[nextVisit.length - 1];
    }
}
