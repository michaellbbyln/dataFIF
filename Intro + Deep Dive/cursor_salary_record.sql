DECLARE
   -- Deklarasi variabel untuk menyimpan total gaji
   v_total_salary NUMBER := 0;

   -- Deklarasi tipe record user-defined sebelum deklarasi cursor
   TYPE rec_city_salary IS RECORD (
      address customers.address%TYPE,
      salary  customers.salary%TYPE
   );

   v_rec rec_city_salary;

   -- Variabel untuk menyimpan kota saat ini yang sedang diproses
   v_current_city customers.address%TYPE;

   -- Cursor untuk ambil data terurut berdasarkan address
   CURSOR cur_city_salaries IS 
       SELECT address, salary 
       FROM customers
       ORDER BY address;

BEGIN
   OPEN cur_city_salaries;
   FETCH cur_city_salaries INTO v_rec;
   WHILE cur_city_salaries%FOUND LOOP
       v_current_city := v_rec.address;
       v_total_salary := 0;

       -- Hitung total gaji untuk satu kota
       WHILE cur_city_salaries%FOUND AND v_rec.address = v_current_city LOOP
           v_total_salary := v_total_salary + v_rec.salary;
           FETCH cur_city_salaries INTO v_rec;
       END LOOP;

       -- Tampilkan hasil
       DBMS_OUTPUT.PUT_LINE('Total Salary in ' || v_current_city || ': ' || v_total_salary);
   END LOOP;
   CLOSE cur_city_salaries;
END;