FasdUAS 1.101.10   ��   ��    k             i         I     �� 	��
�� .aevtoappnull  �   � **** 	 J      ����  ��    k     	 
 
     l     ��  ��    h bset dialog_path to quoted form of "/Users/diegoibarra/Developer/1_myProjects/ShellTestDialog.scpt"     �   � s e t   d i a l o g _ p a t h   t o   q u o t e d   f o r m   o f   " / U s e r s / d i e g o i b a r r a / D e v e l o p e r / 1 _ m y P r o j e c t s / S h e l l T e s t D i a l o g . s c p t "      l     ��������  ��  ��     ��  I    	��  
�� .sysodsct****        scpt  m        �   | / U s e r s / d i e g o i b a r r a / D e v e l o p e r / 1 _ m y P r o j e c t s / S h e l l T e s t D i a l o g . s c p t  �� ��
�� 
plst  J        ��  m       �    b l u e��  ��  ��        l     ��������  ��  ��        l     ��������  ��  ��       !   l      �� " #��   "��
on run {}	activate application "Finder"	tell application "System Events" to tell process "Finder"				--View as Columns		click menu item "as Columns" of menu "View" of menu bar 1				--Check If Groups Activated		set use_groups to ((value of attribute "AXMenuItemMarkChar" of menu item "Use Groups" of menu "View" of menu bar 1) is not missing value)				--Turn Groups Off OR Continue		if use_groups is true then			click menu item "Use Groups" of menu "View" of menu bar 1			log "Toggled Groups OFF"		end if				--Sort UnGrouped by Name		my sortName()				--Turn Groups On		click menu item "Use Groups" of menu "View" of menu bar 1		log "Toggled Groups ON"				--Sort Groups by Kind		my groupKind()			end tellend run    # � $ $� 
 o n   r u n   { }  	 a c t i v a t e   a p p l i c a t i o n   " F i n d e r "  	 t e l l   a p p l i c a t i o n   " S y s t e m   E v e n t s "   t o   t e l l   p r o c e s s   " F i n d e r "  	 	  	 	 - - V i e w   a s   C o l u m n s  	 	 c l i c k   m e n u   i t e m   " a s   C o l u m n s "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1  	 	  	 	 - - C h e c k   I f   G r o u p s   A c t i v a t e d  	 	 s e t   u s e _ g r o u p s   t o   ( ( v a l u e   o f   a t t r i b u t e   " A X M e n u I t e m M a r k C h a r "   o f   m e n u   i t e m   " U s e   G r o u p s "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1 )   i s   n o t   m i s s i n g   v a l u e )  	 	  	 	 - - T u r n   G r o u p s   O f f   O R   C o n t i n u e  	 	 i f   u s e _ g r o u p s   i s   t r u e   t h e n  	 	 	 c l i c k   m e n u   i t e m   " U s e   G r o u p s "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1  	 	 	 l o g   " T o g g l e d   G r o u p s   O F F "  	 	 e n d   i f  	 	  	 	 - - S o r t   U n G r o u p e d   b y   N a m e  	 	 m y   s o r t N a m e ( )  	 	  	 	 - - T u r n   G r o u p s   O n  	 	 c l i c k   m e n u   i t e m   " U s e   G r o u p s "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1  	 	 l o g   " T o g g l e d   G r o u p s   O N "  	 	  	 	 - - S o r t   G r o u p s   b y   K i n d  	 	 m y   g r o u p K i n d ( )  	 	  	 e n d   t e l l  e n d   r u n  !  % & % l     ��������  ��  ��   &  ' ( ' l     ��������  ��  ��   (  )�� ) l      �� * +��   *��on sortName()	set counter to 0	tell application "System Events" to tell process "Finder"		--Sort by Name (Repeat in place for when waiting for menu items to update then Groups Toggled to Off)		repeat until (title of menu item 1 of menu 1 of menu item 7 of menu "View" of menu bar 1) is "Name"			set counter to (counter + 1)			if counter is equal to 1 then log "Waiting until Menu Items Update"			if counter is greater than 100 then error number -128		end repeat		click menu item "Name" of menu "Sort By" of menu item "Sort By" of menu "View" of menu bar 1		log "Sorted by Name"	end tellend sortNameon groupKind()	set counter to 0	tell application "System Events" to tell process "Finder"		--Group by Kind (Repeat in place for when waiting for menu items to update then Groups Toggled to On)		repeat until (title of menu item 1 of menu 1 of menu item 7 of menu "View" of menu bar 1) is "None"			set counter to (counter + 1)			if counter is equal to 1 then log "Waiting until Menu Items Update"			if counter is greater than 100 then error number -128		end repeat		click menu item "Kind" of menu "Group By" of menu item "Group By" of menu "View" of menu bar 1		log "Grouped by Kind"	end tellend groupKind

    + � , ,	�  o n   s o r t N a m e ( )  	 s e t   c o u n t e r   t o   0  	 t e l l   a p p l i c a t i o n   " S y s t e m   E v e n t s "   t o   t e l l   p r o c e s s   " F i n d e r "  	 	 - - S o r t   b y   N a m e   ( R e p e a t   i n   p l a c e   f o r   w h e n   w a i t i n g   f o r   m e n u   i t e m s   t o   u p d a t e   t h e n   G r o u p s   T o g g l e d   t o   O f f )  	 	 r e p e a t   u n t i l   ( t i t l e   o f   m e n u   i t e m   1   o f   m e n u   1   o f   m e n u   i t e m   7   o f   m e n u   " V i e w "   o f   m e n u   b a r   1 )   i s   " N a m e "  	 	 	 s e t   c o u n t e r   t o   ( c o u n t e r   +   1 )  	 	 	 i f   c o u n t e r   i s   e q u a l   t o   1   t h e n   l o g   " W a i t i n g   u n t i l   M e n u   I t e m s   U p d a t e "  	 	 	 i f   c o u n t e r   i s   g r e a t e r   t h a n   1 0 0   t h e n   e r r o r   n u m b e r   - 1 2 8  	 	 e n d   r e p e a t  	 	 c l i c k   m e n u   i t e m   " N a m e "   o f   m e n u   " S o r t   B y "   o f   m e n u   i t e m   " S o r t   B y "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1  	 	 l o g   " S o r t e d   b y   N a m e "  	 e n d   t e l l  e n d   s o r t N a m e    o n   g r o u p K i n d ( )  	 s e t   c o u n t e r   t o   0  	 t e l l   a p p l i c a t i o n   " S y s t e m   E v e n t s "   t o   t e l l   p r o c e s s   " F i n d e r "  	 	 - - G r o u p   b y   K i n d   ( R e p e a t   i n   p l a c e   f o r   w h e n   w a i t i n g   f o r   m e n u   i t e m s   t o   u p d a t e   t h e n   G r o u p s   T o g g l e d   t o   O n )  	 	 r e p e a t   u n t i l   ( t i t l e   o f   m e n u   i t e m   1   o f   m e n u   1   o f   m e n u   i t e m   7   o f   m e n u   " V i e w "   o f   m e n u   b a r   1 )   i s   " N o n e "  	 	 	 s e t   c o u n t e r   t o   ( c o u n t e r   +   1 )  	 	 	 i f   c o u n t e r   i s   e q u a l   t o   1   t h e n   l o g   " W a i t i n g   u n t i l   M e n u   I t e m s   U p d a t e "  	 	 	 i f   c o u n t e r   i s   g r e a t e r   t h a n   1 0 0   t h e n   e r r o r   n u m b e r   - 1 2 8  	 	 e n d   r e p e a t  	 	 c l i c k   m e n u   i t e m   " K i n d "   o f   m e n u   " G r o u p   B y "   o f   m e n u   i t e m   " G r o u p   B y "   o f   m e n u   " V i e w "   o f   m e n u   b a r   1  	 	 l o g   " G r o u p e d   b y   K i n d "  	 e n d   t e l l  e n d   g r o u p K i n d 
 
��       �� - .��   - ��
�� .aevtoappnull  �   � **** . �� ���� / 0��
�� .aevtoappnull  �   � ****��  ��   /   0  �� ��
�� 
plst
�� .sysodsct****        scpt�� 
���kvl ascr  ��ޭ