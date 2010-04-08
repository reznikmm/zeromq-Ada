with Ada.Streams;
with Ada.Finalization;
with Ada.Strings.Unbounded;
with System;
with ZMQ.Messages;
with ZMQ.Contexts;
package ZMQ.Sockets is
   type Socket_Type is
     (P2P,
      PUB,
      SUB,
      REQ,
      REP,
      XREQ,
      XREP,
      UPSTREAM,
      DOWNSTREAM);

   type Socket is new Ada.Finalization.Limited_Controlled with private;

   type Socket_Opt is
     (HWM,   -- Set high water mark
      LWM,   -- Set low water mark
      SWAP,
      AFFINITY,
      IDENTITY,
      SUBSCRIBE,
      UNSUBSCRIBE,
      RATE,
      RECOVERY_IVL,
      MCAST_LOOP,
      SNDBUF,
      RCVBUF);
   type Socket_Flags is mod 2 ** 32;

   function "+" (L, R : Socket_Flags) return Socket_Flags renames "or";

   No_Flags : constant Socket_Flags := 2#0000_0000_0000_0000#;

   not overriding
   procedure Initialize (This         : in out Socket;
                         With_Context : Contexts.Context;
                         Kind         : Socket_Type);

   not overriding
   procedure Bind (This    : in out Socket;
                   Address : String);

   not overriding
   procedure  setsockopt (This    : in out Socket;
                          Option  : Socket_Opt;
                          Value   : String);
   not overriding
   procedure  setsockopt (This    : in out Socket;
                          Option  : Socket_Opt;
                          Value   : Boolean);
   not overriding
   procedure  setsockopt (This    : in out Socket;
                          Option  : Socket_Opt;
                          Value   : Natural);
   not overriding
   procedure setsockopt
     (This    : in out Socket;
      Option  : Socket_Opt;
      Value   : Ada.Streams.Stream_Element_Array);

   not overriding
   procedure  setsockopt (This       : in out Socket;
                          Option     : Socket_Opt;
                          Value      : System.Address;
                          Value_Size : Natural);

   procedure Connect (This    : in out Socket;
                      Address : String);


   not overriding
   procedure Send (This    : in out Socket;
                   Msg     : Messages.Message'Class;
                   Flags   : Socket_Flags := No_Flags);

   not overriding
   procedure Send (This    : in out Socket;
                   Msg     : String;
                   Flags   : Socket_Flags := No_Flags);

   not overriding
   procedure Send (This    : in out Socket;
                   Msg     : Ada.Strings.Unbounded.Unbounded_String;
                   Flags   : Socket_Flags := No_Flags);

   not overriding
   procedure Send (This    : in out Socket;
                   Msg     : Ada.Streams.Stream_Element_Array;
                   Flags   : Socket_Flags := No_Flags);

   not overriding
   procedure Send (This           : in out Socket;
                   Msg_Addres     : System.Address;
                   Msg_Length     : Natural;
                   Flags          : Socket_Flags := No_Flags);


   --  Creates a Message and sends it over the socket.

   generic
      type Element is private;
   procedure Send_Generic (This    : in out Socket;
                           Msg     : Element;
                           Flags   : Socket_Flags := No_Flags);

   --  Send the message over the socet

   not overriding
   procedure flush (This    : in out Socket);

   not overriding
   procedure recv (This    : in out Socket;
                   Msg     : Messages.Message'Class;
                   Flags   : Socket_Flags := No_Flags);


   overriding
   procedure Finalize (this : in out Socket);


   --  function "=" (Left, Right : in Context) return Boolean;

private
   type Socket is new Ada.Finalization.Limited_Controlled with record
      c : System.Address := System.Null_Address;
   end record;
   function img (item : Ada.Streams.Stream_Element_Array) return String;
end ZMQ.Sockets;
