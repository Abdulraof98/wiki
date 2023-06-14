

Table "employees" {
  "id" INT(20) [pk, not null, increment]
  "first_name" varchar(20)
  "last_name" varchar(20)
  "email" varchar(50)
  "phone_no" varchar(20)
  "date_of_join" varchar(10)
  "date_of_birth" varchar(10)
  "salary_type" varchar(10)
  "address" varchar(255)
  "document_id" INT(20)
  "status" INT(1) [not null, default: "1"]
  "create_at" TIMESTAMP
  "updated_at" TIMESTAMP
}

Table "teachers" {
  "id" INT(20) [pk, not null, increment]
  "employee_id" INT(20) [not null]
  }
Table "students" {
  "id" INT(20) [pk, not null, increment]
  "first_name" varchar(50)
  "last_name" varchar(50)
  "gender" varchar(10)
  "date_of_birth" varchar(10)
  "date_of_join" varchar(10)
  "starting_class" varchar(50)
  "address" varchar(255)
  "family_phone_no" varchar(20)
  "document_id" INT(20)
  "status" INT(1) [not null, default: "1"]
  "created_at" TIMESTAMP
  "updated_at" TIMESTAMP
}

Table "subjects" {
  "id" INT(20) [pk, not null, increment]
  "subject_name" varchar(50)
  "fees" INT(10)
  "status" INT(1) [not null, default: "1"]
  "created_at" TIMESTAMP
  "updated_at" TIMESTAMP
}

Table "user_master" {
  "id" INT(20) [pk, not null, increment]
  "user_role" INT(1) [not null, default: "1"]
  "username" varchar(50)
  "password" varchar(255)
  "status" INT(1) [not null, default: "1"]
  "created_at" TIMESTAMP
  "updated_at" TIMESTAMP
}

Table "classes" {
  "id" INT(20) [pk, not null, increment]
  "teacher_id" INT(20) [not null]
  "class_name" varchar(50)
  "start_date" varchar(20)
  "end_date" varchar(20)
  "duration" varchar(20)
  "total_seat" varchar(20)
  "status" INT(1) [not null, default: "1"]
  "created_at" TIMESTAMP
  "updated_at" TIMESTAMP
}

Table "teacher_subject" {
  "id" INT(20) [pk, not null, increment]
  "teacher_id" INT(20) [not null]
  "subject_id" INT(20) [not null]
  "created_at" TIMESTAMP
}

Table "class_student" {
  "id" INT(20) [pk, not null, increment]
  "class_id" INT(20) [not null]
  "student_id" INT(20) [not null]
  "created_at" TIMESTAMP [not null]
}

Table "subject_class" {
  "id" INT(20) [pk, not null, increment]
  "class_id" INT(20) [not null]
  "subject_id" INT(20) [not null]
  "created_at" TIMESTAMP [not null]
}



Table "marks" {
  "id" INT(20) [pk, not null, increment]
  "subject_id" INT(20) [not null]
  "student_id" INT(20) [not null]
  "percentage" varchar(20)
}
Table "mark_details" {
  "id" INT(20) [pk, not null, increment]
  "mark_id" INT(20) [not null]
  "max_marks" INT(20)
  "gained_mark" INT(20)
  "description" varchar(100)
}
Table "fees" {
  "id" INT(20) [pk, not null, increment]
  "class_id" INT(20) [not null]
  "student_id" INT(20) [not null]
  "created_at" TIMESTAMP [not null]
}

Table "installments" {
  "id" INT(20) [pk, not null, increment]
  "fee_id" INT(20) [not null]
  "amont" INT(20)
}
Table "accounts" {
  "id" INT(20) [pk, not null, increment]
  "account_no" varchar(20) [not null]
  "balance" INT(20) [not null]
  "emp_id" INT(20)
}
Table "transactions" {
  "id" INT(20) [pk, not null, increment]
  "account_id" INT(20) [not null]
  "tran_data" INT(20)
  "tran_type" INT(1)
  "ammount" INT(20)
}

Table "tran_type" {
  "id" INT(20) [pk, not null, increment]
  "name" varchar(20) [not null]
}

Table "attendence" {
  "id" INT(20) [pk, not null, increment]
  "subject_id" INT(20) [not null]
  "student_id" INT(20)
  "status" INT(2)
  "date" INT(20)
}
Table "attendence_status" {
  "id" INT(20) [pk, not null, increment]
  "name" varchar(20) [not null]
}
Table "status_type" {
  "id" INT(20) [pk, not null, increment]
  "name" varchar(20) [not null]
}
Ref:"teachers"."id" < "classes"."teacher_id"

Ref:"employees"."id" < "teachers"."employee_id"

Ref:"teachers"."id" < "teacher_subject"."teacher_id"

Ref:"subjects"."id" < "teacher_subject"."subject_id"

Ref:"classes"."id" < "class_student"."class_id"

Ref:"students"."id" < "class_student"."student_id"

Ref:"classes"."id" < "subject_class"."class_id"

Ref:"subjects"."id" < "subject_class"."subject_id"

Ref:"subjects"."id" < "marks"."subject_id"

Ref:"students"."id" < "marks"."student_id"
Ref:"marks"."id" < "mark_details"."mark_id"
Ref:"students"."id" < "fees"."student_id"
Ref:"classes"."id" < "fees"."class_id"
Ref:"employees"."id" < "accounts"."emp_id"
Ref:"accounts"."id" < "transactions"."account_id"
Ref:"tran_type"."id" < "transactions"."tran_type"

Ref:"subjects"."id" < "attendence"."subject_id"

Ref:"students"."id" < "attendence"."student_id"
Ref:"fees"."id" < "installments"."fee_id"
Ref:"attendence_status"."id" < "attendence"."status"
