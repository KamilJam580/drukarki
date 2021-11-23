<?php

 class Toner
{
    public $quantity;
    public $cssStyle;

    function __construct($quantity)
    {
      $this->quantity = 	Formater::FormatQuantity(	$quantity);
      $this->cssStyle=Formater::SelectStyle($this->quantity);  
    }


}

?>