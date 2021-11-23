<?php
class Formater
{
    public static function FormatQuantity($inkQuantity)
    {
      if ($inkQuantity=="-") {
        return " ";
      }
      if ($inkQuantity=="?") {
          return " ";
        }
        //return $inkQuantity;
        return $inkQuantity . "%";
    }
    public static function FormatPageNumber($pages)
    {
          if ($pages>=1000) {
              $len = strlen($pages);
              $pagestousends = substr($pages,0,$len-3);
              $pageshoundreds = substr($pages,$len-3,$len);
              $pages = $pagestousends . "." . $pageshoundreds;              

              return $pages;
          }
          if ($pages==0) {
            return " ";
          }
          return $pages;
    }

    public static function SelectStyle($inkQuantity)
    {
      if ($inkQuantity==" ") {
          return " ";
        }
      if ($inkQuantity<=10) {
        return "low";
      }
      if ($inkQuantity<20) {
        return "mid";
      }
      return "full";
    }
}


?>