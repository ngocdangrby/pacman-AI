# MultiAgents

## Student
Name: Nguyễn Ngọc Đăng
Student ID: 17020077

## Q1: Reflex Agent

Kết quả chạy autograder:  
```bash
Question q1
===========

Pacman emerges victorious! Score: 1236
Pacman emerges victorious! Score: 1218
Pacman emerges victorious! Score: 1234
Pacman emerges victorious! Score: 1234
Pacman emerges victorious! Score: 1208
Pacman emerges victorious! Score: 1230
Pacman emerges victorious! Score: 1209
Pacman emerges victorious! Score: 1245
Pacman emerges victorious! Score: 1243
Pacman emerges victorious! Score: 1235
Average Score: 1229.2
Scores:        1236.0, 1218.0, 1234.0, 1234.0, 1208.0, 1230.0, 1209.0, 1245.0, 1243.0, 1235.0
Win Rate:      10/10 (1.00)
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
*** PASS: test_cases/q1/grade-agent.test (4 of 4 points)
***     1229.2 average score (2 of 2 points)
***         Grading scheme:
***          < 500:  0 points
***         >= 500:  1 points
***         >= 1000:  2 points
***     10 games not timed out (0 of 0 points)
***         Grading scheme:
***          < 10:  fail
***         >= 10:  0 points
***     10 wins (2 of 2 points)
***         Grading scheme:
***          < 1:  fail
***         >= 1:  0 points
***         >= 5:  1 points
***         >= 10:  2 points

### Question q1: 4/4 ###
```
Code: line 82-93

Giải thích:
Sử dụng khoảng cách từ _Pacman_  đến các _Food_ (khoảng cách càng nhỏ càng tốt)
- Do hàm cần viết càng tốt khi _return_ về một điểm cao nên phải sử dụng **1.0/khoảng_cách**.
- Vì mẫu của biểu thức trên là khoảng cách _mahattan_ nên có thể bằng **0**, nên cần cộng vào một hằng số **>0** vào mẫu  số, chọn **+5**.
- Để tránh _Pacman_ chết do gặp _Ghost_, sử dụng một cách tránh xa ghost: nếu khoảng cách từ _Pacman_ đến Ghost <= 2 thì "né ra" bằng cách cho điểm của Action đó âm (chọn **-200**)

## Q2: Minimax

Kết quả chạy autograder:  
```bash
Question q2
===========

*** PASS: test_cases/q2/0-lecture-6-tree.test
*** PASS: test_cases/q2/0-small-tree.test
*** PASS: test_cases/q2/1-1-minmax.test
*** PASS: test_cases/q2/1-2-minmax.test
*** PASS: test_cases/q2/1-3-minmax.test
*** PASS: test_cases/q2/1-4-minmax.test
*** PASS: test_cases/q2/1-5-minmax.test
*** PASS: test_cases/q2/1-6-minmax.test
*** PASS: test_cases/q2/1-7-minmax.test
*** PASS: test_cases/q2/1-8-minmax.test
*** PASS: test_cases/q2/2-1a-vary-depth.test
*** PASS: test_cases/q2/2-1b-vary-depth.test
*** PASS: test_cases/q2/2-2a-vary-depth.test
*** PASS: test_cases/q2/2-2b-vary-depth.test
*** PASS: test_cases/q2/2-3a-vary-depth.test
*** PASS: test_cases/q2/2-3b-vary-depth.test
*** PASS: test_cases/q2/2-4a-vary-depth.test
*** PASS: test_cases/q2/2-4b-vary-depth.test
*** PASS: test_cases/q2/2-one-ghost-3level.test
*** PASS: test_cases/q2/3-one-ghost-4level.test
*** PASS: test_cases/q2/4-two-ghosts-3level.test
*** PASS: test_cases/q2/5-two-ghosts-4level.test
*** PASS: test_cases/q2/6-tied-root.test
*** PASS: test_cases/q2/7-1a-check-depth-one-ghost.test
*** PASS: test_cases/q2/7-1b-check-depth-one-ghost.test
*** PASS: test_cases/q2/7-1c-check-depth-one-ghost.test
*** PASS: test_cases/q2/7-2a-check-depth-two-ghosts.test
*** PASS: test_cases/q2/7-2b-check-depth-two-ghosts.test
*** PASS: test_cases/q2/7-2c-check-depth-two-ghosts.test
*** Running MinimaxAgent on smallClassic 1 time(s).
Pacman died! Score: 84
Average Score: 84.0
Scores:        84.0
Win Rate:      0/1 (0.00)
Record:        Loss
*** Finished running MinimaxAgent on smallClassic after 1 seconds.
*** Won 0 out of 1 games. Average score: 84.000000 ***
*** PASS: test_cases/q2/8-pacman-game.test

### Question q2: 5/5 ###
```

Code: line 149 - 191

Giải thích: 
Tương tự sử dụng giả mã trong SGK:
- _get_agent_turn_: tính xem hiện đang là lượt đi của Agent nào
- _is_pacman_turn_: tính xem hiện có phải lượt đi của Pacman không. Có sử dụng _get_agent_turn_
- _value_: nếu đến lượt Pacman, trả về giá trị của _max_value_.
 Nếu đến lượt Ghost thì trả về giá trị _min_value_.
 Nếu game kết thúc (win or lose) hoặc duyệt đến node lá thì trả về giá trị điểm của
- _max_value_: hàm tính giá trị max cho Pacman
- _min_value_: hàm tính giá trị min cho nhiều Ghost


## Q3: Alpha-Beta Pruning

Kết quả chạy autograder:  
```bash
Question q3
===========

*** PASS: test_cases/q3/0-lecture-6-tree.test
*** PASS: test_cases/q3/0-small-tree.test
*** PASS: test_cases/q3/1-1-minmax.test
*** PASS: test_cases/q3/1-2-minmax.test
*** PASS: test_cases/q3/1-3-minmax.test
*** PASS: test_cases/q3/1-4-minmax.test
*** PASS: test_cases/q3/1-5-minmax.test
*** PASS: test_cases/q3/1-6-minmax.test
*** PASS: test_cases/q3/1-7-minmax.test
*** PASS: test_cases/q3/1-8-minmax.test
*** PASS: test_cases/q3/2-1a-vary-depth.test
*** PASS: test_cases/q3/2-1b-vary-depth.test
*** PASS: test_cases/q3/2-2a-vary-depth.test
*** PASS: test_cases/q3/2-2b-vary-depth.test
*** PASS: test_cases/q3/2-3a-vary-depth.test
*** PASS: test_cases/q3/2-3b-vary-depth.test
*** PASS: test_cases/q3/2-4a-vary-depth.test
*** PASS: test_cases/q3/2-4b-vary-depth.test
*** PASS: test_cases/q3/2-one-ghost-3level.test
*** PASS: test_cases/q3/3-one-ghost-4level.test
*** PASS: test_cases/q3/4-two-ghosts-3level.test
*** PASS: test_cases/q3/5-two-ghosts-4level.test
*** PASS: test_cases/q3/6-tied-root.test
*** PASS: test_cases/q3/7-1a-check-depth-one-ghost.test
*** PASS: test_cases/q3/7-1b-check-depth-one-ghost.test
*** PASS: test_cases/q3/7-1c-check-depth-one-ghost.test
*** PASS: test_cases/q3/7-2a-check-depth-two-ghosts.test
*** PASS: test_cases/q3/7-2b-check-depth-two-ghosts.test
*** PASS: test_cases/q3/7-2c-check-depth-two-ghosts.test
*** Running AlphaBetaAgent on smallClassic 1 time(s).
Pacman died! Score: 84
Average Score: 84.0
Scores:        84.0
Win Rate:      0/1 (0.00)
Record:        Loss
*** Finished running AlphaBetaAgent on smallClassic after 1 seconds.
*** Won 0 out of 1 games. Average score: 84.000000 ***
*** PASS: test_cases/q3/8-pacman-game.test

### Question q3: 5/5 ###
```

Code: line 201 - 246 

Giải thích: 
Tương tự sử dụng giả mã trong SGK, tương tự **Q2**:
- _get_agent_turn_: tính xem hiện đang là lượt đi của Agent nào
- _is_pacman_turn_: tính xem hiện có phải lượt đi của Pacman không. Có sử dụng _get_agent_turn_
- _value_: nếu đến lượt Pacman, trả về giá trị của _max_value_.
 Nếu đến lượt Ghost thì trả về giá trị _min_value_.
 Nếu game kết thúc (win or lose) hoặc duyệt đến node lá thì trả về giá trị điểm của
- _max_value_: hàm tính giá trị max cho Pacman
- _min_value_: hàm tính giá trị min cho nhiều Ghost

    Điểm khác:
   - Sử dụng Alpha và Beta để tìm min,max
   - Alpha: tốt nhất của Max
   - Beta: tốt nhất của Min
## Q4: Reflex Agent

Kết quả chạy autograder:  
```bash
Question q4
===========

*** PASS: test_cases/q4/0-expectimax1.test
*** PASS: test_cases/q4/1-expectimax2.test
*** PASS: test_cases/q4/2-one-ghost-3level.test
*** PASS: test_cases/q4/3-one-ghost-4level.test
*** PASS: test_cases/q4/4-two-ghosts-3level.test
*** PASS: test_cases/q4/5-two-ghosts-4level.test
*** PASS: test_cases/q4/6-1a-check-depth-one-ghost.test
*** PASS: test_cases/q4/6-1b-check-depth-one-ghost.test
*** PASS: test_cases/q4/6-1c-check-depth-one-ghost.test
*** PASS: test_cases/q4/6-2a-check-depth-two-ghosts.test
*** PASS: test_cases/q4/6-2b-check-depth-two-ghosts.test
*** PASS: test_cases/q4/6-2c-check-depth-two-ghosts.test
*** Running ExpectimaxAgent on smallClassic 1 time(s).
Pacman died! Score: 84
Average Score: 84.0
Scores:        84.0
Win Rate:      0/1 (0.00)
Record:        Loss
*** Finished running ExpectimaxAgent on smallClassic after 1 seconds.
*** Won 0 out of 1 games. Average score: 84.000000 ***
*** PASS: test_cases/q4/7-pacman-game.test

### Question q4: 5/5 ###
```

Code: line 201 - 246 

Giải thích: 
Tương tự sử dụng giả mã trong SGK, tương tự **Q2**:
- _get_agent_turn_: tính xem hiện đang là lượt đi của Agent nào
- _is_pacman_turn_: tính xem hiện có phải lượt đi của Pacman không. Có sử dụng _get_agent_turn_
- _value_: nếu đến lượt Pacman, trả về giá trị của _max_value_.
 Nếu đến lượt Ghost thì trả về giá trị _min_value_.
 Nếu game kết thúc (win or lose) hoặc duyệt đến node lá thì trả về giá trị điểm của
- _max_value_: hàm tính giá trị max cho Pacman
- _min_value_: hàm tính giá trị min cho nhiều Ghost

    Điểm khác:
   - Thay vì sử dụng _min_value_, ở đây sử dụng _exp_value_
để tính điểm cho Ghost
   - Sử dụng giả mã như SGK
   - p = xác suất của các đường = **1.0/ số actions**

## Q5: Reflex Agent

Kết quả chạy autograder:  
```bash
Question q5
===========

Pacman emerges victorious! Score: 1338
Pacman emerges victorious! Score: 1371
Pacman emerges victorious! Score: 1345
Pacman emerges victorious! Score: 1204
Pacman emerges victorious! Score: 1339
Pacman emerges victorious! Score: 1280
Pacman emerges victorious! Score: 1358
Pacman emerges victorious! Score: 1147
Pacman emerges victorious! Score: 1342
Pacman emerges victorious! Score: 1358
Average Score: 1308.2
Scores:        1338.0, 1371.0, 1345.0, 1204.0, 1339.0, 1280.0, 1358.0, 1147.0, 1342.0, 1358.0
Win Rate:      10/10 (1.00)
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
*** PASS: test_cases/q5/grade-agent.test (6 of 6 points)
***     1308.2 average score (2 of 2 points)
***         Grading scheme:
***          < 500:  0 points
***         >= 500:  1 points
***         >= 1000:  2 points
***     10 games not timed out (1 of 1 points)
***         Grading scheme:
***          < 0:  fail
***         >= 0:  0 points
***         >= 10:  1 points
***     10 wins (3 of 3 points)
***         Grading scheme:
***          < 1:  fail
***         >= 1:  1 points
***         >= 5:  2 points
***         >= 10:  3 points

### Question q5: 6/6 ###
```

Code: line 201 - 246 

Giải thích: 
- Do hàm này trả về điểm của state, càng cao thì càng tốt, nên các giá trị có sử dụng khoảng cách manhattan thì đều được dùng chung công thức: **(1.0/khoảng_cách_manhattan) * trọng_số**
  - **_trọng_số_**: thể hiện độ quan trọng của đích đến đó (càng lớn thì càng ưu tiên => ăn trước)
- Sử dụng khoảng cách _mahattan_ của _Pacman_ đến các _bigFood_, khoảng cách càng gần thì càng tốt, sử dụng: **(1.0/kc_manhattan_từ_Pac->bigFood) * trọng_số = 200** 
- Sử dụng khoảng cách _mahattan_ của _Pacman_ đến các _Food_, khoảng cách càng gần thì càng tốt, sử dụng **(1.0/kc_manhattan_từ_Pac->Food) * trọng_số = 10**
- Khi _scaredTimes_ > 3 (tránh rượt "quá đà", không rút kịp)thì truy đuổi ma bằng cách tăng trọng số **(1.0/kc_manhattan_từ_Pac->Ghost) * trọng_số = 1000**
- Thêm né ma khi _scareTimes_ == 0 bằng cách return âm khi gần ma (khoảng cách <=2) 
- Trả về tổng các giá trị trên và state.getScore()

## Tổng kết

```bash
Provisional grades
==================
Question q1: 4/4
Question q2: 5/5
Question q3: 5/5
Question q4: 5/5
Question q5: 6/6
------------------
Total: 25/25
```