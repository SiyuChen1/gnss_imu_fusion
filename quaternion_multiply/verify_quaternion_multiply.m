E1 = [pi/2,0,pi/4];
% note: point instead of frame !!!
quat1 = quaternion(E1,'euler','ZYX','point');
R1 = rotmat(quat1,'point');

R1_ref = rotx(45) * rotz(90);
R1 - R1_ref

E2 = [pi/3,pi/6,pi/3];
quat2 = quaternion(E2,'euler','ZYX', 'point');
R2 = rotmat(quat2,'point');

R = R2 * R1;
quat = quaternion(R,'rotmat','point');

q_m = quat1 * quat2;
[qw1, qx1, qy1, qz1] = parts(quat1);
[qw2, qx2, qy2, qz2] = parts(quat2);
q1 = [qw1, qx1, qy1, qz1];
q2 = [qw2, qx2, qy2, qz2];

q_n = quaternion(q_multiply(q1, q2));

q_m - q_n