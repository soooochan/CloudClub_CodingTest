import java.util.*;

class Solution {
    int N = 9;
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    boolean[] visited = new boolean[N];
    
    public String solution(String rny_string) {
        String answer = "";

        // 그래프 만들기, visited 초기화 부분은 위에 쓴 DFS와 동일
        
        // 1부터 시작, 로직은 동일
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;
        int now = 0;
        
        while (!queue.isEmpty()) {
            now = queue.poll();
            System.out.println(now);
            for(Integer next : graph.get(now)) {
                if (visited[next] == false) {
                    queue.offer(next);
                    visited[next] = true;
                }
            }
        }
        
        return answer;
    }
}