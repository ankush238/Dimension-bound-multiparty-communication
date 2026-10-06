clear all

d=2;
M0v = sdpvar(d,d,'hermitian','real'); 
M1v = sdpvar(d,d,'hermitian','real'); 
conM = [M0v>=0; M1v>=0; M0v+M1v == eye(d)];

A1v = sdpvar(d,d,'hermitian','real');
A2v = sdpvar(d,d,'hermitian','real');
A3v = sdpvar(d,d,'hermitian','real'); 
condA=[A1v>=0;A2v>=0;A3v>=0;trace(A1v)==1;trace(A2v)==1;trace(A3v)==1];

B1v = sdpvar(d^2,d^2,'hermitian','real');
B2v = sdpvar(d^2,d^2,'hermitian','real');
B3v = sdpvar(d^2,d^2,'hermitian','real');
condB = [B1v>=0;B2v>=0;B3v>=0;PartialTrace(B1v,2) == eye(d);PartialTrace(B2v,2) == eye(d); PartialTrace(B3v,2) == eye(d)];

A1=RandomDensityMatrix(d);
A2=RandomDensityMatrix(d);
A3=RandomDensityMatrix(d);

X1 = RandomSuperoperator(2); B1=ChoiMatrix(X1);
X2 = RandomSuperoperator(2); B2=ChoiMatrix(X2);
X3 = RandomSuperoperator(2); B3=ChoiMatrix(X3);


%      P11 -P12 -P13 -P21 +P22 -P23 -P31 -P32 +P33    Facdt ineq 9
ops = sdpsettings('solver','sdpt3','verbose',0);
for iter = 1:25

    obj_M= trace( kron((A1)',M0v)*B1-kron((A1)',M0v)*B2+kron((A1)',M0v)*B3+kron((A2)',M0v)*B2-2*kron((A2)',M0v)*B3-2*kron((A3)',M0v)*B1+kron((A3)',M0v)*B2+2*kron((A3)',M0v)*B3);
    game_M=optimize(conM,-real(obj_M),ops);
    M0=value(M0v);
    M1=value(M1v);

    obj_A=  trace( kron((A1v)',M0)*B1-kron((A1v)',M0)*B2+kron((A1v)',M0)*B3+kron((A2v)',M0)*B2-2*kron((A2v)',M0)*B3-2*kron((A3v)',M0)*B1+kron((A3v)',M0)*B2+2*kron((A3v)',M0)*B3);
    game_A=optimize(condA,-real(obj_A),ops);
    A1=value(A1v);
    A2=value(A2v);
    A3=value(A3v);

    obj_B= trace( kron((A1)',M0)*B1v-kron((A1)',M0)*B2v+kron((A1)',M0)*B3v+kron((A2)',M0)*B2v-2*kron((A2)',M0)*B3v-2*kron((A3)',M0)*B1v+kron((A3)',M0)*B2v+2*kron((A3)',M0)*B3v);
    game_B=optimize(condB,-real(obj_B),ops);
    B1=value(B1v);
    B2=value(B2v);
    B3=value(B3v);
end
value(obj_M)
%value(obj_A)
%value(obj_B)
