

package body ZMQ.Examples.JSON_Data is

   --  =========================================================================
   --    Coordinate
   --  =========================================================================

   Coordinate_X_Name : constant String := "X";
   Coordinate_Y_Name : constant String := "Y";
   Coordinate_Z_Name : constant String := "Z";
   ------------
   -- Create --
   ------------
   function Create (Val : Coordinate) return JSON_Value is
   begin
      return Ret : constant JSON_Value := Create_Object do
         Ret.Set_Field (Coordinate_X_Name, Create (Val.X));
         Ret.Set_Field (Coordinate_Y_Name, Create (Val.Y));
         Ret.Set_Field (Coordinate_Z_Name, Create (Val.Z));
      end return;
   end Create;

   ---------------
   -- Set_Field --
   ---------------

   procedure Set_Field
     (Val        : JSON_Value;
      Field_Name : UTF8_String;
      Field      : Coordinate)
   is
   begin
      Val.Set_Field (Field_Name, Create (Field));
   end Set_Field;

   -------------------
   -- Cb_Coordinate --
   -------------------

   procedure Cb_Coordinate
     (User_Object : in out Coordinate;
      Name        : UTF8_String;
      Value       : JSON_Value)
   is
   begin
      if Name = Coordinate_X_Name then
         User_Object.X := Value.Get;
      elsif Name = Coordinate_Y_Name then
         User_Object.Y := Value.Get;
      elsif Name = Coordinate_Z_Name then
         User_Object.Z := Value.Get;
      end if;
   end Cb_Coordinate;


   --  =========================================================================
   --    Data_Type
   --  =========================================================================
   Data_Type_Sensor_Name_Name  : constant String := "Sensor_Name";
   Data_Type_OK_Name           : constant String := "OK";
   Data_Type_Location_Name     : constant String := "Location";
   Data_Type_Orientation_Name  : constant String := "Orientation";
   ------------
   -- Create --
   ------------

   function Create (Val : Data_Type) return JSON_Value is
   begin
      return Ret : constant JSON_Value := Create_Object do
         Ret.Set_Field (Data_Type_Sensor_Name_Name, Create (Val.Sensor_Name));
         Ret.Set_Field (Data_Type_OK_Name, Create (Val.OK));
         Ret.Set_Field (Data_Type_Location_Name, Create (Val.Location));
         Ret.Set_Field (Data_Type_Orientation_Name, Create (Val.Orientation));
      end return;
   end Create;

   ---------------
   -- Set_Field --
   ---------------

   procedure Set_Field
     (Val        : JSON_Value;
      Field_Name : UTF8_String;
      Field      : Data_Type)
   is
   begin
      Val.Set_Field (Field_Name, Create (Field));
   end Set_Field;

   ------------------
   -- Cb_Data_Type --
   ------------------

   procedure Cb_Data_Type
     (User_Object : in out Data_Type;
      Name        : UTF8_String;
      Value       : JSON_Value)
   is
   begin
      if Name = Data_Type_Sensor_Name_Name then
         User_Object.Sensor_Name := Value.Get;
      elsif Name = Data_Type_OK_Name then
         User_Object.OK := Value.Get;
      elsif Name = Data_Type_Location_Name then
         Read (Value, Cb_Coordinate'Access, User_Object.Location);
      elsif Name = Data_Type_Orientation_Name then
         Read (Value, Cb_Coordinate'Access, User_Object.Orientation);
      end if;
   end Cb_Data_Type;

   procedure  Read (Src : JSON_Value; Into : in out Data_Type) is
   begin
      Read (Src, Cb_Data_Type'Access, Into);
   end Read;

end ZMQ.Examples.JSON_Data;
