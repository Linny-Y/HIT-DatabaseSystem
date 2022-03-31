
-- ----------------------------
-- Table structure for faculty
-- ----------------------------
DROP TABLE IF EXISTS `faculty`;
CREATE TABLE `faculty`  (
    `fno` varchar(4) NOT NULL COMMENT '学院编号',
    `fname` varchar(30) NOT NULL COMMENT '学院名称',
    primary key (`fno`)
)COMMENT '学院';

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
    `cno` varchar(10) NOT NULL COMMENT '班级编号',
    `grade` varchar(10) NOT NULL COMMENT '年级',
    `num` INTEGER COMMENT '人数',
    `fno` varchar(4) NOT NULL COMMENT '学院编号',
    primary key (`cno`),
    foreign key (`fno`) references `faculty`(`fno`)
)COMMENT '班级';

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
    `sno` varchar(20) NOT NULL COMMENT '学号',
    `sname` varchar(40) NOT NULL COMMENT '学生姓名',
    `ssex` varchar(2) check `ssex` in('男','女') NOT NULL COMMENT '学生性别',
    `sbirthday` DATE NOT NULL COMMENT '出生日期',
    `sphone` varchar(15) COMMENT '电话号码',
    `saddress` varchar(200) COMMENT '家庭住址',
    `cno` varchar(10) NOT NULL COMMENT '班级编号',
    primary key (`sno`),
    foreign key (`cno`) references `class`(`cno`)
)COMMENT '学生';

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
    `tno` varchar(20) NOT NULL COMMENT '教师工号',
    `tname` varchar(40) NOT NULL COMMENT '教师姓名',
    `tpost` varchar(10) NOT NULL COMMENT '职称',
    `tdegree` varchar(10) NOT NULL COMMENT '学位',
    primary key (`tno`)
)COMMENT '教师';

-- ----------------------------
-- Table structure for employment
-- ----------------------------
DROP TABLE IF EXISTS `employment`;
CREATE TABLE `employment`  (
    `tno` varchar(20) NOT NULL COMMENT '教师工号',
    `fno` varchar(4) NOT NULL COMMENT '学院编号',
    `etime` DATE NOT NULL COMMENT '聘用日期',
    primary key (`tno`,`fno`),
    foreign key (`tno`) references `teacher`(`tno`),
    foreign key (`fno`) references `faculty`(`fno`)
)COMMENT '聘用';

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
    `courseno` varchar(20) NOT NULL COMMENT '课程号',
    `coursename` varchar(20) NOT NULL COMMENT '课程名称',
    `credit` INTEGER NOT NULL COMMENT '学分',
    `hour` INTEGER NOT NULL COMMENT '课时',
    `facultyno` varchar(4) NOT NULL COMMENT '开课学院编号',
    primary key (`courseno`),
    foreign key (`facultyno`) references `faculty`(`fno`)
)COMMENT '课程';

-- ----------------------------
-- Table structure for schedule
-- ----------------------------
DROP TABLE IF EXISTS `schedule`;
CREATE TABLE `schedule`  (
    `courseno` varchar(20) NOT NULL COMMENT '课程号',
    `scheduleno` varchar(20) NOT NULL COMMENT '开课班号',
    `year` year NOT NULL COMMENT '年份',
    `semester` varchar(2) NOT NULL COMMENT '学期',
    `capacity` INTEGER NOT NULL COMMENT '选课容量',
    `snum` INTEGER DEFAULT 0 COMMENT '选课人数',
    check (`semester`in('春','夏','秋')),
    check (`snum`<`capacity`),
    primary key (`scheduleno`),
    foreign key (`courseno`) references `course`(`courseno`)
)COMMENT '课程安排';

-- ----------------------------
-- Table structure for teach
-- ----------------------------
DROP TABLE IF EXISTS `teach`;
CREATE TABLE `teach`  (
    `scheduleno` varchar(20) NOT NULL COMMENT '开课班号',
    `teacherno` varchar(20) NOT NULL COMMENT '教师工号',
    primary key (`scheduleno`,`teacherno`),
    foreign key (`scheduleno`) references `schedule`(`scheduleno`),
    foreign key (`teacherno`) references `teacher`(`tno`)
)COMMENT '教师任教';

-- ----------------------------
-- Table structure for classroom
-- ----------------------------
DROP TABLE IF EXISTS `classroom`;
CREATE TABLE `classroom`  (
    `classroomno` varchar(20) NOT NULL COMMENT '教室编号',
    `building` varchar(10) NOT NULL COMMENT '所在教学楼名称',
    `roomcapacity` INTEGER NOT NULL COMMENT '教室容量',
    primary key (`classroomno`)
)COMMENT '教室';

-- ----------------------------
-- Table structure for time
-- ----------------------------
DROP TABLE IF EXISTS `time`;
CREATE TABLE `time`  (
    `courseno` varchar(20) NOT NULL COMMENT '课程号',
    `scheduleno` varchar(20) NOT NULL COMMENT '开课班号',
    `time` varchar(1) check (`time`in('1','2','3','4','5','6')) NOT NULL COMMENT '上课时间',
    `classroomno` varchar(20) NOT NULL COMMENT '教室编号',
    primary key (`courseno`,`scheduleno`,`time`),
    foreign key (`scheduleno`) references `schedule`(`scheduleno`),
    foreign key (`courseno`) references `course`(`courseno`),
    foreign key (`classroomno`) references `classroom`(`classroomno`)
)COMMENT '时间教室安排';

-- ----------------------------
-- Table structure for choose
-- ----------------------------
DROP TABLE IF EXISTS `choose`;
CREATE TABLE `choose`  (
    `studentno` varchar(20) NOT NULL COMMENT '学号',
    `courseno` varchar(20) NOT NULL COMMENT '课程号',
    `scheduleno` varchar(20) NOT NULL COMMENT '开课班号',
    `teacherno` varchar(20) NOT NULL COMMENT '教师工号',
    `score` INTEGER COMMENT '成绩',
    `recorddate` datetime COMMENT '成绩上传时间',
    primary key (`studentno`,`courseno``scheduleno`),
    foreign key (`studentno`) references `student`(`sno`),
    foreign key (`courseno`) references `course`(`courseno`),
    foreign key (`scheduleno`) references `schedule`(`scheduleno`),
    foreign key (`teacherno`) references `teacher`(`tno`)
)COMMENT '选课';
