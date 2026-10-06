d=2;
A1v=sdpvar(d,d,'hermitian','complex');
A2v=sdpvar(d,d,'hermitian','complex');
A3v=sdpvar(d,d,'hermitian','complex');
conA=[A1v>=0;A2v>=0;A3v>=0;trace(A1v)==1;trace(A2v)==1;trace(A3v)==1];

B1v=sdpvar(d,d,'hermitian','complex');
B2v=sdpvar(d,d,'hermitian','complex');
B3v=sdpvar(d,d,'hermitian','complex');
conB=[B1v>=0;B2v>=0;B3v>=0;trace(B1v)==1;trace(B2v)==1;trace(B3v)==1];

M0v=sdpvar(d^2,d^2,'hermitian','complex');
M1v=sdpvar(d^2,d^2,'hermitian','complex');
conM=[M0v>=0;M1v>=0; M0v+M1v==eye(d^2)];

A1=RandomDensityMatrix(d); B1=RandomDensityMatrix(d);
A2=RandomDensityMatrix(d); B2=RandomDensityMatrix(d);
A3=RandomDensityMatrix(d); B3=RandomDensityMatrix(d);

% p00 + p01 + p02 + 2p10 − 2p11 − p12 − p20 − 2p21 + 2p22

ops = sdpsettings('solver', 'sdpt3', 'verbose', 0);
for iter =1:35
    obj_state= trace(M0v*(kron(A1,B1)+kron(A1,B2)+kron(A1,B3)+2*kron(A2,B1)-2*kron(A2,B2)-kron(A2,B3)-kron(A3,B1)-2*kron(A3,B2)+2*kron(A3,B3)));
    game_M=optimize(conM,-real(obj_state),ops);
    M0=value(M0v);
    M1=value(M1v);

    obj_A=  trace(M0*(kron(A1v,B1)+kron(A1v,B2)+kron(A1v,B3)+2*kron(A2v,B1)-2*kron(A2v,B2)-kron(A2v,B3)-kron(A3v,B1)-2*kron(A3v,B2)+2*kron(A3v,B3)));
    game_A=optimize(conA,-real(obj_A),ops);
    A1=value(A1v);
    A2=value(A2v);
    A3=value(A3v);
    
    obj_B= trace(M0*(kron(A1,B1v)+kron(A1,B2v)+kron(A1,B3v)+2*kron(A2,B1v)-2*kron(A2,B2v)-kron(A2,B3v)-kron(A3,B1v)-2*kron(A3,B2v)+2*kron(A3,B3v)));
    game_B=optimize(conB,-real(obj_B),ops);
    B1=value(B1v);
    B2=value(B2v);
    B3=value(B3v);
end
value(obj_B)
