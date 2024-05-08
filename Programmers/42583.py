def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 다리의 길이를 크기로 갖는 큐를 만들고 0을 채운다.
    bridge = [0 for i in range(bridge_length)]
    bridge_weight = 0
    
    # 대기 중인 트럭이 없을 때까지 한 번에 한 대씩 트럭을 IN-OUT한다. 
    # 트럭의 무게가 넘치면 0을 IN한다. 
    while truck_weights:
        truck_out = bridge.pop(0)
        bridge_weight -= truck_out
        
        if bridge_weight + truck_weights[0] <= weight:
            truck_in = truck_weights.pop(0)
            bridge.append(truck_in)
            bridge_weight += truck_in
        else:
            bridge.append(0)
            
        answer += 1
            
    # 마지막 트럭이 다리를 모두 지날 때까지 기다린다.
    answer += bridge_length
    
    return answer
