u:Gem::SpecificationQ["
1.3.7i"	hirbU:Gem::Version["
0.4.0u:	Time���    "^A mini view framework for console/irb that's easy to use, even while under its influence.U:Gem::Requirement[[[">=U; ["0U;[[[">=U; ["
1.3.5"	ruby[	o:Gem::Dependency
:@requirementU;[[[">=U; ["
1.1.0:@prereleaseF:@version_requirements@ :
@name"
bacon:
@type:developmento;
;	U;[[[">=U; ["0;
F;@*;"
mocha;;o;
;	U;[[[">=U; ["0;
F;@4;"mocha-on-bacon;;o;
;	U;[[[">=U; ["0;
F;@>;"bacon-bits;;"tagaholic"gabriel.horner@gmail.com["Gabriel Horner"�Hirb provides a mini view framework for console applications and uses it to improve ripl(irb)'s default inspect output. Given an object or array of objects, hirb renders a view based on the object's class and/or ancestry. Hirb offers reusable views in the form of helper classes. The two main helpers, Hirb::Helpers::Table and Hirb::Helpers::Tree, provide several options for generating ascii tables and trees. Using Hirb::Helpers::AutoTable, hirb has useful default views for at least ten popular database gems i.e. Rails' ActiveRecord::Base. Other than views, hirb offers a smart pager and a console menu. The smart pager only pages when the output exceeds the current screen size. The menu is used in conjunction with tables to offer two dimensional menus."http://tagaholic.me/hirb/T@["MIT